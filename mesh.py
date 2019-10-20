#!/usr/bin/env python

"""Defining mesh
"""
import numpy as np

class Mesh():
	def __init__(self,length,nb_element):
		elements,coordinates = create_1D_mesh(length,nb_element)
		self.mesh = {"elements" : elements, "coordinates" : coordinates}

def create_1D_mesh(length,nb_element):
	elements = np.array([[0,1]])
	coordinates = np.array([[0,0]])
	x = np.linspace(0.0,length,nb_element)
	for i in range(1,nb_element):
		elements = np.concatenate((elements,np.array([[i,i+1]])))
		coordinates = np.concatenate((coordinates,np.array([[x[i],0]])))
	elements = np.delete(elements,-1,0)

	return elements,coordinates
