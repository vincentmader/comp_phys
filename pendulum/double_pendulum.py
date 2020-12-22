from tqdm import tqdm

import matplotlib.pyplot as plt
from numpy import cos, sin, pi
from scipy.integrate import RK45


y0 = [pi, pi, 1e-2, 0]
t0, t_bound = 0, 10000
first_step, max_step = 1e-1, 1e-1

L, m, g = 1, 1, 1
steps = 10000


def f(t, y):

    th_1, th_2 = y[0], y[1]
    p_1, p_2 = y[2], y[3]
    dth = th_1 - th_2

    dth_1 = 6/(m * L**2) * (2*p_1 - 3*cos(dth) * p_2) / (16 - 9*cos(dth)**2)
    dth_2 = 6/(m * L**2) * (8*p_2 - 3*cos(dth) * p_1) / (16 - 9*cos(dth)**2)
    dp_1 = -m * L**2 / 2 * (dth_1 * dth_2 * sin(dth) + 3*g/L*sin(th_1))
    dp_2 = -m * L**2 / 2 * (-dth_1 * dth_2 * sin(dth) + g/L*sin(th_2))

    return [dth_1, dth_2, dp_1, dp_2]


def integrate(steps):

    integrator = RK45(
        f, t0, y0, t_bound, first_step=first_step, max_step=max_step
    )

    ys = []
    for _ in tqdm(range(steps)):
        y = integrator.step()
        ys.append(integrator.y)

    return ys


def plot(ys):

    for idx in tqdm(range(len((ys)))):
        y = ys[idx]
        th_1, th_2 = y[0], y[1]
        p_1, p_2 = y[2], y[3]

        x_1, y_1 = L * sin(th_1), -L * cos(th_1)
        x_2, y_2 = x_1 + L * sin(th_2), y_1 - L * cos(th_2)

        plt.figure(figsize=(5, 5))
        plt.xlim(-2.1, 2.1)
        plt.ylim(-2.1, 2.1)
        plt.xticks([])
        plt.yticks([])

        plt.plot([0, x_1], [0, y_1], color='k')
        plt.plot([x_1, x_2], [y_1, y_2], color='k')
        c1 = plt.Circle((x_1, y_1), 0.05, color='k')
        c2 = plt.Circle((x_2, y_2), 0.05, color='k')
        plt.gca().add_artist(c1)
        plt.gca().add_artist(c2)

        formatted_idx = idx
        if idx < 1000:
            formatted_idx = f'0{formatted_idx}'
            if idx < 100:
                formatted_idx = f'0{formatted_idx}'
                if idx < 10:
                    formatted_idx = f'0{formatted_idx}'

        plt.savefig(f'./figures/{formatted_idx}.png')
        plt.close()


def main():
    ys = integrate(steps)
    plot(ys)


if __name__ == "__main__":
    main()
