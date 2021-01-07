import numpy as np

from .integrate import main as integrate
from .display import main as display


y0 = [
    0, 0, 0, 0, 0, 0,  # 3 position & 3 velocity values for 1. body
    0, 1, 0, 1, 0, 0,  # 3 position & 3 velocity values for 2. body
]
ms = [1000, 1]


def main(steps=500, run_integrator=True):

    if run_integrator:
        ys = integrate(y0, ms, steps)
        np.savetxt('./n_body/out/ys.txt', ys)
    else:
        ys = np.loadtxt('./n_body/out/ys.txt')

    display(ys)


if __name__ == "__main__":
    main()
