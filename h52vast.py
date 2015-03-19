# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:18:34 2015

@author: jingpeng
"""
#%% parameters
import numpy as np

Dir = '/usr/people/jingpeng/seungmount/Omni/TracerTasks/Daan_Piriform_cortex_Corrections/VAST/chunk_2_segments/'
filename ='chunk_2_Segment.h5'
tifname = 'chunk_2_Segment.tif'

#%% read the data
import h5py
f = h5py.File(Dir + filename )
vol = np.asarray(f['/main'])

vol = np.asarray(vol* ((2**24-1)/float(vol.max())), dtype='uint32') 
rgb = np.zeros( np.append(np.array( vol.shape ), 3), dtype='uint8')

rgb[:,:,:, 0] = np.remainder( vol, 256)
rgb[:,:,:, 1] = np.remainder( vol, 25536) / 256
rgb[:,:,:, 2] = vol / 25536

#%% write as tiff
import tifffile
tifffile.imsave(Dir + tifname, rgb)
