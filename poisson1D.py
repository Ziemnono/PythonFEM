#!/usr/bin/env python

"""1D poisson problem
"""
import numpy as np
from scipy import integrate, misc
import mesh
import matplotlib


def linear_shape_function(x):
	dx = x[1]-x[0]
	index = np.arange(x.shape[0])
	sf = np.array([])
	fct = lambda y : 1-(y-np.where(y == 0))
	for x_index,x_value in np.ndenumerate(x):
		if x_value==0:
			sf = np.append(sf,np.piecewise(x, [x <= x_value, x > x_value], [fct(x_value)[0][0], 0]))
		# else:
		# 	print(x[0])
		# 	sf = np.append(sf,np.piecewise(x, [x < x[0],
		# 		x[0] < x <= x[1],
		# 		x >= x_value], [-10, 5,10]))
	print(sf)
def main():
	length = 1.0
	nb_element = 5

	geometry = mesh.Mesh(length, nb_element)
	x = geometry.mesh["coordinates"][:,0]
	linear_shape_function(x)

	x2 = lambda x: x
	print(integrate.quad(x2,0,1))
	print(misc.derivative(x2,0))

if __name__ == '__main__':
	main()