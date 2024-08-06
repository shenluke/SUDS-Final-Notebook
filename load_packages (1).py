from __future__ import print_function, division
import brutus
#Import packages needed
from brutus import utils as butils
from brutus import seds
from brutus import filters 

from six.moves import range
import numpy as np
import scipy
import matplotlib
from matplotlib import pyplot as plt
import h5py
# plot in-line within the notebook
#%matplotlib inline

# re-defining plotting defaults
from matplotlib import rcParams
rcParams.update({'xtick.major.pad': '7.0'})
rcParams.update({'xtick.major.size': '7.5'})
rcParams.update({'xtick.major.width': '1.5'})
rcParams.update({'xtick.minor.pad': '7.0'})
rcParams.update({'xtick.minor.size': '3.5'})
rcParams.update({'xtick.minor.width': '1.0'})
rcParams.update({'ytick.major.pad': '7.0'})
rcParams.update({'ytick.major.size': '7.5'})
rcParams.update({'ytick.major.width': '1.5'})
rcParams.update({'ytick.minor.pad': '7.0'})
rcParams.update({'ytick.minor.size': '3.5'})
rcParams.update({'ytick.minor.width': '1.0'})
rcParams.update({'axes.titlepad': '15.0'})
rcParams.update({'axes.labelpad': '15.0'})
rcParams.update({'font.size': 30})
#Loading Filters
# all filters
print('All bands:', filters.FILTERS,'\n')

# just Pan-STARRS and 2MASS
filt = filters.ps[:-2] + filters.tmass
print('Current subset:', filt)
nnfile = '/home/jupyter-lukeshen/lukeshen/DATAFILE/nn_c3k.h5'
mist_iso = '/home/jupyter-lukeshen/lukeshen/DATAFILE/MIST_1.2_iso_vvcrit0.0.h5'
#Loading needed files
isochrone = seds.Isochrone(filters=filt, nnfile=nnfile, mistfile=mist_iso)
mist_eeptrk = '/home/jupyter-lukeshen/lukeshen/DATAFILE/MIST_1.2_EEPtrk.h5'
import pickle

# initialize our core simulator object: the SEDmaker
fname = '/home/jupyter-lukeshen/my_folder/sbi_sedmaker.pkl'
try:
  # try to load a saved version if possible
  with open(fname, 'rb') as f:
    sedmaker = pickle.load(f)
except:
  # if not, just make a new one and dump it to disk
  sedmaker = seds.SEDmaker(filters=filt, nnfile=nnfile, mistfile=mist_eeptrk)
  with open(fname, 'wb') as f:
    pickle.dump(sedmaker, f)
print(sedmaker)    