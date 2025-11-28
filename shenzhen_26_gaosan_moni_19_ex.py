import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq


def main():
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

    x, a_sym = sp.symbols('x a', real=True, positive=True)

    f_expr = 3 * x * (-1 + sp.log(x)) - sp.Rational(1, 2) * x**2 + sp.Rational(27, 2) - 9 * sp.log(3) - a_sym * (x - 3)

    f_prime_expr = 3 * sp.log(x) - x - a_sym

    f_func = sp.lambdify((x, a_sym), f_expr, 'numpy')
    f_prime_func = sp.lambdify((x, a_sym), f_prime_expr, 'numpy')

    a_min = 0.0
    a_max = float(3 * np.log(3) - 3)
    a_vals = np.linspace(a_min + 1e-6, a_max - 1e-6, 100)

    sum_f1_f2 = []
    sum_f1_f6mx1 = []
    x1_plus_x2 = []

    for a_val in a_vals:
        def fp(x): return f_prime_func(x, a_val)

        # Find left root x1 in (small, 3)
        x1 = brentq(fp, 1e-6, 3.0)

        # Find right root x2 in (3, upper)
        x2 = brentq(fp, 3.0, 20.0)

        f1 = f_func(x1, a_val)
        f2 = f_func(x2, a_val)

        sum_f1_f2.append(f1 + f2)

        f6mx1 = f_func(6 - x1, a_val)
        sum_f1_f6mx1.append(f1 + f6mx1)

        x1_plus_x2.append(x1 + x2)

    sum_f1_f2 = np.array(sum_f1_f2)
    sum_f1_f6mx1 = np.array(sum_f1_f6mx1)
    x1_plus_x2 = np.array(x1_plus_x2)

    _, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))

    ax1.plot(a_vals, sum_f1_f2, 'b-', label=r'$f(x_1)+f(x_2)$')
    ax1.set_xlabel('a')
    ax1.set_ylabel(r'$f(x_1)+f(x_2)$')
    ax1.set_title(r'$f(x_1)+f(x_2)$ 随a变化的曲线')
    ax1.grid(True)
    ax1.legend()

    ax2.plot(a_vals, sum_f1_f6mx1, 'r-', label=r'$f(x_1)+f(6-x_1)$')
    ax2.set_xlabel('a')
    ax2.set_ylabel(r'$f(x_1)+f(6-x_1)$')
    ax2.set_title(r'$f(x_1)+f(6-x_1)$ 随a变化的曲线')
    ax2.grid(True)
    ax2.legend()

    ax3.plot(a_vals, sum_f1_f2, 'b-', label=r'$f(x_1)+f(x_2)$')
    ax3.plot(a_vals, sum_f1_f6mx1, 'r--', label=r'$f(x_1)+f(6-x_1)$')
    ax3.set_xlabel('a')
    ax3.set_ylabel('函数值之和')
    ax3.set_title(r'两条曲线对比')
    ax3.grid(True)
    ax3.legend()

    ax4.plot(a_vals, x1_plus_x2, 'g-', label=r'$x_1 + x_2$')
    ax4.set_xlabel('a')
    ax4.set_ylabel(r'$x_1 + x_2$')
    ax4.set_title(r'$x_1 + x_2$ 随a变化的曲线')
    ax4.grid(True)
    ax4.axhline(6, color='k', linestyle='--', linewidth=0.8, label=r'$x_1+x_2=6$')
    ax4.legend()

    plt.tight_layout(h_pad=0.2)
    plt.show()

    # Now plot f(x) + f(6 - x) vs x for a few representative a values
    a_examples = [0.1, (a_min + a_max) / 2, a_max * 0.9]
    x_plot = np.linspace(0.1, 5.9, 500)  # avoid x=0 (log undefined) and x=6 where 6-x=0

    plt.figure(figsize=(8, 6))
    for a_val in a_examples:
        f_vals = f_func(x_plot, a_val)
        f6mx_vals = f_func(6 - x_plot, a_val)
        total = f_vals + f6mx_vals
        plt.plot(x_plot, total, label=f'a = {a_val:.3f}')

    plt.xlabel('x')
    plt.ylabel(r'$f(x) + f(6 - x)$')
    plt.title(r'$f(x) + f(6 - x)$ 图像（与a无关）')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
