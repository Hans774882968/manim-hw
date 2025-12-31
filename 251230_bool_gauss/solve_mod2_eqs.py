import itertools
import numpy as np


def brute_force():
    equations = [
        ([1, 1, 0, 1, 0, 0, 0, 0, 0], 1),  # a0 + a1 + a3 = 1
        ([1, 1, 1, 0, 1, 0, 0, 0, 0], 0),  # a0 + a1 + a2 + a4 = 0
        ([0, 1, 1, 0, 0, 1, 0, 0, 0], 0),  # a1 + a2 + a5 = 0
        ([1, 0, 0, 1, 1, 0, 1, 0, 0], 0),  # a0 + a3 + a4 + a6 = 0
        ([0, 1, 0, 1, 1, 1, 0, 1, 0], 0),  # a1 + a3 + a4 + a5 + a7 = 0
        ([0, 0, 1, 0, 1, 1, 0, 0, 1], 0),  # a2 + a4 + a5 + a8 = 0
        ([0, 0, 0, 1, 0, 0, 1, 1, 0], 0),  # a3 + a6 + a7 = 0
        ([0, 0, 0, 0, 1, 0, 1, 1, 1], 0),  # a4 + a6 + a7 + a8 = 0
        ([0, 0, 0, 0, 0, 1, 0, 1, 1], 0),  # a5 + a7 + a8 = 0
    ]

    def check_solution(sol):
        """检查解是否满足所有方程"""
        for coeffs, rhs in equations:
            lhs = sum(c * s for c, s in zip(coeffs, sol)) % 2
            if lhs != rhs:
                return False
        return True

    solutions = []
    for bits in itertools.product([0, 1], repeat=9):
        if check_solution(bits):
            solutions.append(bits)

    print(f"法1：找到 {len(solutions)} 个解：")
    for i, sol in enumerate(solutions):
        weight = sum(sol)
        print(f"解 {i+1}: {sol}, 按下次数: {weight}")

    if solutions:
        min_weight = min(sum(sol) for sol in solutions)
        min_solutions = [sol for sol in solutions if sum(sol) == min_weight]
        print(f"\n最少按下次数: {min_weight}")
        print(f"对应的解 ({len(min_solutions)} 个):")
        for sol in min_solutions:
            positions = []
            for idx, val in enumerate(sol):
                if val == 1:
                    row = idx // 3 + 1
                    col = idx % 3 + 1
                    positions.append(f"({row},{col})")
            print(f"  {positions}")


def gauss():
    A = np.array([
        [1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 1]
    ], dtype=int)
    b = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int)
    Ab = np.concatenate((A, b.reshape(-1, 1)), axis=1) % 2

    def gauss_elim_gf2(Ab):
        """
        在 GF(2) 上对增广矩阵 Ab 进行高斯-若尔当消元。
        """
        m, n = Ab.shape
        n_vars = n - 1
        row = 0
        col = 0
        pivot_cols = []

        while row < m and col < n_vars:
            pivot_row = None
            for r in range(row, m):
                if Ab[r, col] == 1:
                    pivot_row = r
                    break

            if pivot_row is None:
                col += 1
                continue

            if pivot_row != row:
                Ab[[row, pivot_row]] = Ab[[pivot_row, row]]

            pivot_cols.append(col)

            for r in range(m):
                if r != row and Ab[r, col] == 1:
                    Ab[r] = (Ab[r] + Ab[row]) % 2

            row += 1
            col += 1

        for r in range(row, m):
            if Ab[r, :-1].sum() % 2 == 0 and Ab[r, -1] == 1:
                raise ValueError("方程组无解")

        return Ab, pivot_cols

    reduced_Ab, pivot_cols = gauss_elim_gf2(Ab.copy())

    print("法2：行简化阶梯形增广矩阵:")
    print(reduced_Ab)
    print("\n主元列:", pivot_cols)

    n_vars = 9
    x_particular = np.zeros(n_vars, dtype=int)
    for i, col in enumerate(pivot_cols):
        x_particular[col] = reduced_Ab[i, -1]

    print("\n一个特解 x_p:")
    for i, val in enumerate(x_particular):
        print(f"a{i} = {val}")

    weight = np.sum(x_particular)
    print(f"\n该特解的权重（按下的次数）: {weight}")

    free_cols = [c for c in range(n_vars) if c not in pivot_cols]
    print(f"\n自由变量列: {free_cols}")

    if free_cols:
        min_weight = np.inf
        best_solution = None
        num_free = len(free_cols)
        for combo in range(2**num_free):
            free_vals = [(combo >> i) & 1 for i in range(num_free)]

            x = x_particular.copy()
            for idx, col in enumerate(free_cols):
                x[col] = free_vals[idx]

            current_weight = np.sum(x)
            if current_weight < min_weight:
                min_weight = current_weight
                best_solution = x.copy()

        print(f"\n最小权重解:")
        for i, val in enumerate(best_solution):
            print(f"a{i} = {val}")
        print(f"最小按下的次数: {min_weight}")
    else:
        print(f"\n解唯一，最小按下的次数为: {weight}")


if __name__ == "__main__":
    brute_force()
    print('-' * 30)
    gauss()
