# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:18:34 2015

@author: jingpeng
"""
#%% parameters
import numpy as np

Dir = '/usr/people/bds2/seungmount/Omni/TracerTasks/Piriform_cortex_Corrections/Chunk_07/Chunk_07_EM/'
filename ='chunk_07_em'
tifname = 'chunk_07_em.tif'

isgray = True

#%% read the data
import h5py
f = h5py.File(Dir + filename )
invol = np.asarray(f['/main'])
f.close()

if isgray:
	outvol = (invol-invol.min()) / (invol.max()-invol.min()) * 255
	outvol = outvol.astype('uint8')
else:
	vol = np.asarray(invol* ((2**24-1)/float(invol.max())), dtype='uint32') 
	rgb = np.zeros( np.append(np.array( invol.shape ), 3), dtype='uint8')

	rgb[:,:,:, 0] = np.remainder( invol, 256)
	rgb[:,:,:, 1] = np.remainder( invol, 25536) / 256
	rgb[:,:,:, 2] = invol / 25536

#%% write as tiff
import tifffile
tifffile.imsave(Dir + tifname, outvol)

