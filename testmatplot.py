#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import sys
import getopt

def simpleTest():
	#产生测试数据 
	x = np.arange(1,10) 
	y = x 
	fig = plt.figure() 
	ax1 = plt.subplot(211) 
	ax1.set_title('Scatter Plot') 
	plt.xlabel('X') 
	plt.ylabel('Y') 
	ax1.scatter(x,y,c = 'r',marker = 'o') 
	plt.legend('x1') 
	plt.show() 

	#产生测试数据 
	x = np.arange(1,100) 
	y = x * x
	ax1.set_title('Scatter Plot')
	plt.xlabel('X')
	plt.ylabel('Y')
	lValue = 1
	ax1.scatter(x,y,c='r',s= 10, linewidths=lValue, marker='<') 
	plt.legend('x1') 
	plt.show()

def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)

def simpleTest3():
	# for i,color in enumerate("rgby"):
	# 	plt.subplot(221+i)
	# plt.show()

	t1 = np.arange(0, 5, 0.1)
	t2 = np.arange(0, 5, 0.02)

	plt.figure(12)
	plt.subplot(221)
	plt.plot(t1, f(t1), 'bo', t2, f(t2), 'r--')

	plt.subplot(222)
	plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')

	# 对比看下223 和 212 的效果 也就是subplot始终是全局的划分
	# plt.subplot(223)
	plt.subplot(212)
	plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
	plt.show()

	# plt.subplot(221)
	# # equivalent but more general
	# ax1=plt.subplot(2, 2, 1)
	# # add a subplot with no frame
	# ax2=plt.subplot(222, frameon=False)
	# # add a polar subplot
	# plt.subplot(223, projection='polar')
	# # add a red subplot that shares the x-axis with ax1
	# plt.subplot(224, sharex=ax1, facecolor='red')
	# #delete ax2 from the figure
	# plt.delaxes(ax2)
	# #add ax2 to the figure again
	# plt.subplot(ax2)


def simpleTest2():
	# Simple data to display in various forms
	x = np.linspace(0, 2 * np.pi, 400)
	y = np.sin(x ** 2)
	plt.close('all')
	# Just a figure and one subplot
	f, ax = plt.subplots()
	ax.plot(x, y)
	ax.set_title('Simple plot')

	# Two subplots, the axes array is 1-d
	f, axarr = plt.subplots(2, sharex=True)
	axarr[0].plot(x, y)
	axarr[0].set_title('Sharing X axis')
	axarr[1].scatter(x, y)

	# Two subplots, unpack the axes array immediately
	f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
	ax1.plot(x, y)
	ax1.set_title('Sharing Y axis')
	ax2.scatter(x, y)

	# Three subplots sharing both x/y axes
	f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=True)
	ax1.plot(x, y)
	ax1.set_title('Sharing both axes')
	ax2.scatter(x, y)
	ax3.scatter(x, 2 * y ** 2 - 1, color='r')
	# Fine-tune figure; make subplots close to each other and hide x ticks for
	# all but bottom plot.
	f.subplots_adjust(hspace=0)
	plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

	# row and column sharing
	f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
	ax1.plot(x, y)
	ax1.set_title('Sharing x per column, y per row')
	ax2.scatter(x, y)
	ax3.scatter(x, 2 * y ** 2 - 1, color='r')
	ax4.plot(x, 2 * y ** 2 - 1, color='r')

	# Four axes, returned as a 2-d array
	f, axarr = plt.subplots(2, 2)
	axarr[0, 0].plot(x, y)
	axarr[0, 0].set_title('Axis [0,0]')
	axarr[0, 1].scatter(x, y)
	axarr[0, 1].set_title('Axis [0,1]')
	axarr[1, 0].plot(x, y ** 2)
	axarr[1, 0].set_title('Axis [1,0]')
	axarr[1, 1].scatter(x, y ** 2)
	axarr[1, 1].set_title('Axis [1,1]')
	# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
	plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
	plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

	# Four polar axes
	f, axarr = plt.subplots(2, 2, subplot_kw=dict(projection='polar'))
	axarr[0, 0].plot(x, y)
	axarr[0, 0].set_title('Axis [0,0]')
	axarr[0, 1].scatter(x, y)
	axarr[0, 1].set_title('Axis [0,1]')
	axarr[1, 0].plot(x, y ** 2)
	axarr[1, 0].set_title('Axis [1,0]')
	axarr[1, 1].scatter(x, y ** 2)
	axarr[1, 1].set_title('Axis [1,1]')
	# Fine-tune figure; make subplots farther from each other.
	f.subplots_adjust(hspace=0.3)

	plt.show()

# simpleTest()
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
            simpleTest3()
        except getopt.error, msg:
             raise Usage(msg)
        # more code, unchanged
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())