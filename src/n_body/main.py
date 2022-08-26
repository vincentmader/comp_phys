import os

import numpy as np
from numpy import sqrt

from .integrate import main as integrate
from .display import main as display
from .display import pyplot as display_via_pyplot
from utils.physics_utils import kepler_velocity as v_K

M = 1
m = 1e-4

def rotate_y0(y0, dphi):

    new_y0 = []

    nr_of_bodies = int(len(y0) / 6)
    for i in range(nr_of_bodies):

        x, y = y0[6*i+2], y0[6*i+3]
        u, v = y0[6*i+4], y0[6*i+5]
        r = (x**2 + y**2)**.5
        phi = np.arctan2(y, x) + dphi
        x, y = r * np.cos(phi), r * np.sin(phi)

        w = (u**2 + v**2)**.5
        rho = np.arctan2(v, u) + dphi
        u, v = w * np.cos(rho), w * np.sin(rho)

        for j in [y0[6*i], y0[6*i+1], x, y, u, v]:
            new_y0.append(j)
    return new_y0

# chaotic solar system
# y0 = [
#     M,    1,   0, 0,   0, 0,  # mass, radius, 2 pos. & 2 vel. values
#     1e-6, 1,   0.25, 0,   0, v_K(0.25),
#     1e-6, 1,   .6, 0,   0, v_K(.6),
#     1e-6, 1,   .2, 0,   0, v_K(.11),
#     1e-6, 1,   0, .2,    -v_K(.12), 0,
#     1e-6, 1,   -.4, 0,   0, -v_K(.4),
#     1e-6, 1,   .7, 0,   0, v_K(.7),
#     1e-6, 1,   -.6, 0,    0, -v_K(.6),
#     1e-6, 1,   -.9, 0,    0, -v_K(1),
# ]

# 4 planets, same elliptical orbital parameters, at different angle
# y0 = [
#     M,    1,   0,   0,   0, 0,  # mass, radius, 2 pos. & 2 vel. values
#     1e-5, 1,  .6,   0,    0, kepler_velocity(2),
#     1e-5, 1, -.6,   0,   0, -kepler_velocity(2),
#     1e-5, 1,   0,  .6,   -kepler_velocity(2), 0,
#     1e-5, 1,   0, -.6,   kepler_velocity(2), 0,
# ]


# choreography
N = 24
y0 = [  # polar
    M, 1,   0, 0,   0, 0,
]
for i in range(N):
    phi = i / N * 2 * np.pi
    for j in [m, 1,   1, phi,   v_K(3), np.pi/2 + phi]:
        y0.append(j)
# 3 body
# ================================================================
# y0 = [
#     M, 1,       0, 0,   0, 0,
#     1e-9, 1,       .8, 0,  v_K(.8), np.pi / 2,
#     # 1e-10, 1,   .85, 0,  v_K(.9) + v_K(.1, m=1e-2), np.pi / 2,
# ]
# three kepler planets
# y0 = [
#     M, 1,       .8, 0,           .7, np.pi/2,
#     M, 1,       .8, 2*np.pi/3,   .7, np.pi/2 + 2*np.pi/3,
#     M, 1,       .8, 4*np.pi/3,   .7, np.pi/2 + 4*np.pi/3,
# ]
# figure 8 (y0 is cartesian)
# p1, p2 = 0.347111, 0.532728
# y0 = [
#     M, 1,  -1, 0,   p1, p2,
#     M, 1,   0, 0,   -2*p1, -2*p2,
#     M, 1,   1, 0,   p1, p2,
# ]
# y0 = rotate_y0(y0, .68)
# centauri
# y0 = [
#     M,    1,   -.1, 0,   0, -v_K(.4),  # mass, radius, 2 pos. & 2 vel. values
#     M,    1,    .1, 0,   0, v_K(.4),  # mass, radius, 2 pos. & 2 vel. values
#     1e-6, 1,   -.9, 0,   0, -1.4,
# ]

# =======
# crazy 4 stars
# y0 = [
#     M,    1,   -.25, 0,   0, -2.8,  # mass, radius, 2 pos. & 2 vel. values
#     M,    1,    .25, 0,   0, 2.8,  # mass, radius, 2 pos. & 2 vel. values
#     # mass, radius, 2 pos. & 2 vel. values
#     M,    1,     0, -.25,   0, 2.8,
#     # mass, radius, 2 pos. & 2 vel. values
#     M,    1,     0, .25,    0, -2.8,
# ]

# asteroids, TODO: needs more chaos -> random init
# m = 1e-5
# y0 = [
#     M, 1,   0,  0,  0, 0,
#     m, 1,   1,  0,  0, v_K(2),
#     m, 1,   -1, 0,  0, -v_K(2),
#     m, 1,   .8, 0,  0, v_K(2),
#     m, 1,   -.8, 0,   0, -v_K(2),
#     m, 1,   .6, 0,  0, v_K(2),
#     m, 1,   -.6, 0,   0, -v_K(2),
#     m, 1,   .4, 0,  0, v_K(2),
#     m, 1,   -.4, 0,   0, -v_K(2),
# ]


def main(nr_of_steps=2000, run_integrator=True, screenshot_mode=False):

    def increment_out_file_name(out_file_dir, out_file_name):
        while True:
            if f'{out_file_name}.txt' in os.listdir(out_file_dir):
                out_file_name = f'ys_{int(out_file_name.split("_")[1][-4:]) + 1}'
            else:
                return out_file_name

    out_file_dir, out_file_name = './n_body/out', 'ys_0'
    out_file_name = increment_out_file_name(out_file_dir, out_file_name)

    if run_integrator:
        ys = integrate(y0, nr_of_steps, y0_is_in_polar_coords=True)
        np.savetxt(os.path.join(out_file_dir, f'{out_file_name}.txt'), ys)
    else:
        ys = np.loadtxt('./n_body/out/sym/sym_24.txt')
        # np.savetxt(os.path.join(out_file_dir, out_file_name), ys)

    display_via_pyplot(ys)
    display(ys, screenshot_mode=screenshot_mode)
