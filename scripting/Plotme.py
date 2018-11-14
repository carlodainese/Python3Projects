import matplotlib.pyplot as plt
import time

def plot(timelist, savefig):
    x = [k for k in range (len(timelist))]
    y = timelist

    xint = list(map(int, x))
    yint = list(map(float, y))

    plt.plot(xint,yint, 'o')
    plt.show()
    if (savefig):
        plt.savefig('/home/cd/PycharmProjects/siti/images/ping-{}.png'.format(time.time()))
        print('image saved on disk!')


def plot_save(plt, savefig):
    if (savefig):
        plt.savefig('/home/cd/PycharmProjects/siti/images/ping-{}.png'.format(time.time()))
        print('image saved on disk!')