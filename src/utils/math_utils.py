import numpy as np


def l2_norm(vec):
    return np.sqrt(sum([i**2 for i in vec]))


def transform_coords_cart2pol(x, y):
    r = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return r, phi


def transform_coords_pol2cart(r, phi):
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return x, y


def rotate_2D_cartesian_vector(x, y, dphi):
    r, phi = transform_coords_cart2pol()
    phi += dphi
    x, y = transform_coords_pol2cart(r, phi)
    return x, y
