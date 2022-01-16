import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema
from tqdm import tqdm

from integrate import Grid, Pars
from integrate import main as integrate


EPSILON = 1e-4
SIGMA = 0.2
T_MAX = 10

# initialize parameters
pars = Pars()
pars.Nx = 100
pars.x1 = -1
pars.x2 = 1
pars.cs = 1
pars.cfl = 0.4

# intitial conditions
x = np.linspace(pars.x1, pars.x2, pars.Nx)
rho_0 = 1 + EPSILON * np.exp(-x**2 / (2*SIGMA**2))
u_0 = np.array([0] * pars.Nx)

INTEGRATE = False


def main():

    if INTEGRATE:
        pars.tmax = T_MAX

        # create grid and set initial conditions
        grid = Grid(pars)
        grid.cons = np.array([rho_0, u_0])

        # run
        rhos, us = integrate(grid, pars)

        np.savetxt('./testing/sound_pulse_rhos.txt', rhos)
        np.savetxt('./testing/sound_pulse_us.txt', us)
    else:
        rhos = np.loadtxt('./testing/sound_pulse_rhos.txt')
        us = np.loadtxt('./testing/sound_pulse_us.txt')

    print(len(rhos))
    for idx, (rho, u) in enumerate(zip(rhos, us)):
        #     print(rho, u)

        # for i in tqdm(range(11)):
        #     tmax = i * tcs
        #     rho, u = integrate(tmax)
        #     label = r'$t_{max}=' + str(i) + '\cdot t_{c_s}$'
        #     label = r'$t_{max}=0$' if not i else label
        #     plt.xlim(x[0], x[-1])
        plt.plot(x, rho)
        plt.show()
        # plt.ylim(1-1e-5, 1e-4)

    # plt.legend()
        # plt.savefig('./testing/figures/out.pdf')
        # plt.close()
        # input()


main()
