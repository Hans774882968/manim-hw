import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import os

file_dir = os.path.dirname(__file__)
pyvis_html_path = os.path.join(file_dir, '2x2开关阵列状态转移图.html')

# 按位置0 → 影响 0,1,2 其他同理
press_effect = [
    [0, 1, 2],
    [0, 1, 3],
    [0, 2, 3],
    [1, 2, 3]
]

G = nx.Graph()

for state in range(16):
    G.add_node(state)

for state in range(16):
    for button in range(4):
        new_state = state
        for pos in press_effect[button]:
            new_state ^= (1 << pos)
        G.add_edge(state, new_state, button=button)

source_state = 0
target_state = 8   # 0b1000

shortest_path_nodes = nx.shortest_path(G, source=source_state, target=target_state)
shortest_path_edges = [(shortest_path_nodes[i], shortest_path_nodes[i + 1]) for i in range(len(shortest_path_nodes) - 1)]

plt.figure(figsize=(12, 10))

pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=800, node_color='lightblue')
nx.draw_networkx_edges(G, pos, edge_color='gray', width=1)

nx.draw_networkx_nodes(G, pos, nodelist=shortest_path_nodes, node_size=800, node_color='lightgreen')
nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='lightgreen', width=3)

labels = {node: format(node, '04b') for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_weight='bold')

nt = Network(bgcolor='hsl(231, 15%, 18%)')
for node in G.nodes():
    label = format(node, '04b')
    if node in shortest_path_nodes:
        nt.add_node(node, label=label, color='lightgreen', shape='circle', title=f"状态{label}（在最短路上）")
    else:
        nt.add_node(node, label=label, color='lightblue', shape='circle', title=f"状态{label}")

for u, v, data in G.edges(data=True):
    button = data.get('button', -1)
    if (u, v) in shortest_path_edges or (v, u) in shortest_path_edges:
        nt.add_edge(u, v, color='lightgreen', value=1.5, title=f"按开关{button}")
    else:
        nt.add_edge(u, v, color='white', value=1, title=f"按开关{button}")
nt.show(pyvis_html_path, notebook=False)

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.title("2x2开关阵列状态转移图\n"
          "点：4位二进制数。边：按下某个位置的按钮。高亮路径: 从0000到1000的最短路")
plt.axis('off')
plt.tight_layout()
plt.show()
