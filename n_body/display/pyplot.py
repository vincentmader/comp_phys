import matplotlib.pyplot as plt
import numpy as np


def main(ys):

    nr_of_bodies = int(len(ys[0]) / 8)

    # make plot
    for i in range(nr_of_bodies):

        x = [j[8*i+2] for j in ys]
        y = [j[8*i+3] for j in ys]

        plt.plot(x, y, label=i, color='white')

    # plt.xticks([-2, -1, 0, 1, 2])
    # plt.yticks([-2, -1, 0, 1, 2])
    plt.xticks([])
    plt.yticks([])
    # plt.legend()

    # dark mode
    fig, ax = plt.gcf(), plt.gca()
    fig.patch.set_facecolor('#222222')
    ax.set_facecolor('#222222')
    ax.title.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    plt.xticks(color='white')
    plt.yticks(color='white')
    # legend = plt.legend(frameon=True)
    # for text in legend.get_texts():
    #     text.set_color('white')
    # frame = legend.get_frame()
    # frame.set_facecolor('#222222')
    # frame.set_edgecolor('white')

    # save
    plt.savefig('../static/media/pyplots/nbody_2.pdf')
    plt.savefig('../static/media/pyplots/nbody_2.png')
    plt.close()

    # =================
