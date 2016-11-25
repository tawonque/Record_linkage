#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 14:37:18 2016

@author: Tavo
"""
#Import packages, notice the 'recordlinkage' package
#and the geographic packeges 'geopy', 'ogr', 'gdal', 'shapely'
#not sure yet which one will be useful

import os
import numpy as np
import pandas as pd
import recordlinkage as rl
import jellyfish
import ogr
import gdal

from geopy import distance
from shapely.geometry import Point, MultiPolygon
from shapely.wkt import dumps, loads

import math
import sys

#---------------------
#Create a function to calculate distance between two geographic coordinates
#Might change and adapt depending on what we need when comparing data location
   
def sphereDistance(from_point, to_point):
    #Calculate distance between from_point.x and from_point.y and \
    #to_point.x and to+_point.y
    distance.VincentyDistance.ELLIPSOID = 'WGS-84'
    return distance.distance((from_point.x, from_point.y), \
                             (to_point.x, to_point.y))

#----------------------
#Create two dataframes

A = {
    'name': ['Joe', 'John', 'Louis', 'Kenneth', 'Mary', 'Joseph']
    }
A = pd.DataFrame(A) 
A['lastname'] = ['Smith', 'Perez', 'Hughes', 'Hughes', 'Peres', 'Louis']
A['age'] = [12, 19, 55, 32, 32, 72]
A['sex'] = ['M', 'M', 'M', 'M', 'F', 'M']
A['lat'] = [0.23, 10.54, 45.98, 23.43, 10.55, 65.21]
A['lon'] = [110.32, -66.98, 10.12, 45.45, -66.96, 32.04]
A.index.name = 'A' #notice that I add a name to the index, necessary for rl

B = {
    'name': ['Gus', 'John', 'Lewis', 'Joanne', 'Robin', 'Margaret']
    }
B = pd.DataFrame(B) 
B['lastname'] = ['Smith', 'Clayton', 'Smith', 'Payne', 'Smith', 'Taylor']
B['age'] = [11, 34, 32, 21, 56, 72]
B['sex'] = ['M', 'M', 'M', 'F', 'F', 'F']
B['lat'] = [0.23, 10.54, 45.98, 23.43, 10.55, 65.21]
B['lon'] = [110.32, -66.98, 10.12, 45.45, -66.96, 32.04]
B.index.name = 'B' #notice that I add a name to the index, necessary for rl

print()
print(A)
print()
print(B)

#-------------------
#Record linkage

A = A #specify the dataframes to compare
B = B #specify the dataframes to compare

index = rl.Pairs(A, B)
candidate_links = index.block('lastname')

compare = rl.Compare(candidate_links, A, B)

'''
compare.string('name', 'name', method='jarowinkler', threshold=0.85)'''
compare.exact('sex', 'sex')
compare.exact('age', 'age')


