from PIL import Image
import numpy as np
import torch
import sys, os

## Set up
ftype  = '.tif' # File type to be saved
dtype  = torch.FloatTensor
tmpdir = 'tmp/'
if not os.path.exists(tmpdir):
  os.makedirs(tmpdir)
# dtype = torch.cuda.FloatTensor # Uncomment if using GPU

## File paths
r_channel  = '/path/to/red-channel'
g_channel  = '/path/to/green-channel'
b_channel  = '/path/to/blue-channel'
af_channel = '/path/to/af-channel'
r_channel  = 'data/epcam-lrp6/CH4.tif'
g_channel  = 'data/epcam-lrp6/CH2.tif'
b_channel  = 'data/epcam-lrp6/CH1.tif'
af_channel = 'data/epcam-lrp6/CH3.tif'

## Channel names
r_name = 'lrp6'
g_name = 'epcam'
b_name = 'dapi'

## Prep data
data = dict(zip(['r_channel', 'g_channel', 'b_channel', 'af_channel'], [r_channel, g_channel, b_channel, af_channel]))

for i, k in enumerate(data):
  tmp = np.array(Image.open(data[k]))
  if len(tmp.shape) == 3:
    tmp = tmp[:, :, i]
  elif len(tmp.shape) == 2:
    if tmp.max() > 1:
      tmp = 255 * (tmp - tmp.min()) / (tmp.max() - tmp.min())
  data[k] = tmp


## Model parameters
reg_lambda, reg_alpha = .4, .4

tolbreak = True