import os

SRT_FILE = r"media\bili\n2_n2_mod_12_eq_0\n2_n2_mod_12_eq_0.srt"

# 替换规则：从左到右依次替换。注意，子串需要靠后排
REPLACEMENTS = [
    ("汉斯", "Hans"),
    ("（u=3", "（u=3）"),
    ("n减1乘n乘n加1", "(n-1)n(n+1)"),
    ("n减2", "n-2"),
    ("n方乘n方减1乘n方减4", r"n^2(n^2-1)(n^2-4)"),
    ("n减3", "n-3"),
    ("4的阶乘", "4!"),
    ("6的阶乘（720", "6!（720）"),
    ("n方乘n方减1乘n+2", r"n^2(n^2-1)(n+2)"),
    ("n方乘n方减1", r"n^2(n^2-1)"),
    ("5的阶乘（120", "5!（120）"),
]


def fix_subtitle(input_path):
    if not os.path.exists(input_path):
        print(f"❌ 文件不存在: {input_path}")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    for old, new in REPLACEMENTS:
        content = content.replace(old, new)

    # 如果有改动，写回文件
    if content != original_content:
        with open(input_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"√ 已完成替换并保存到: {input_path}")
    else:
        print("ℹ️ 未发现需要替换的内容，文件未修改~")


if __name__ == "__main__":
    fix_subtitle(SRT_FILE)
