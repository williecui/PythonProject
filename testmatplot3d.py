#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sys
import getopt

def test3dSurface():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v)) 
    ax.plot_surface(x, y, z, color='b')
    plt.show()

def test3dLine():
    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z**2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    ax.plot(x, y, z, label='parametric curve')
    ax.legend()
    plt.show()

def tet3dContour():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X, Y, Z = axes3d.get_test_data(0.05)
    cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
    cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)
     
    ax.set_xlabel('X')
    ax.set_xlim(-40, 40)
    ax.set_ylabel('Y')
    ax.set_ylim(-40, 40)
    ax.set_zlabel('Z')
    ax.set_zlim(-100, 100)
    plt.show()

def test3dWire():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Grab some test data.
    X, Y, Z = axes3d.get_test_data(0.05)
    # Plot a basic wireframe.
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    plt.show()


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
            # simpleTest()
            # simpleTest2()
            # test3dSurface()
            # test3dLine()
            # tet3dContour()
            test3dWire()
        except getopt.error, msg:
             raise Usage(msg)
        # more code, unchanged
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())