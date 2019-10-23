# import sys
# Math
import numpy as np
# import math

#Images
# import copy
# import tqdm
from PIL import Image
# import cv2

# IO
import os

from pathlib import Path

data_folder = '/home/oamir2013/train/'
out_folder =  '/home/oamir2013/train_texture1/'
tiles_folder = '/home/oamir2013/tiles_20/'

print('train_texture')

def listFilesRecursivily(data_folder):
  q = len(data_folder)
  result = [os.path.join(dp, f)[q:] for dp, dn, filenames in os.walk(data_folder) for f in filenames if os.path.splitext(f)[1] == '.jpg']
  return result
file_list = listFilesRecursivily(data_folder)

def openImagePath(path):
  img = Image.open(path)
  return np.asarray(img)
def openImage(file_ix):
  return openImagePath(data_folder + file_list[file_ix])
def saveImage(np_img, ix):
  im = Image.fromarray(np.uint8(np_img))
  im.save(out_folder+file_list[ix])
def tileAreas(tile_img):
  return np.mean(tile_img[:10,:10]), np.mean(tile_img[:10,10:]), \
         np.mean(tile_img[10:,:10]), np.mean(tile_img[10:,10:])

tiles = listFilesRecursivily(tiles_folder)
tile_imgs = [openImagePath(tiles_folder+tile) for tile in tiles]
tile_imgs_means = [tileAreas(tile) for tile in tile_imgs]
del tiles

# Tweak the takings of means
def diffWindowTile(means_window, tile_img_means):
  return  (means_window[0,0]-tile_img_means[0])**2 + (means_window[0,1]-tile_img_means[1])**2 + \
          (means_window[1,0]-tile_img_means[2])**2 + (means_window[1,1]-tile_img_means[3])**2
def closestWindow(window):
  closest_item = 0
  closest_value = diffWindowTile(window, tile_imgs_means[0])
  for i in range(1,len(tile_imgs)):
    diff = diffWindowTile(window, tile_imgs_means[i])
    if diff < closest_value:
      closest_value = diff
      closest_item = i
  return closest_item
def MosaicTileEffectPic(image):
  H,W,C = image.shape
  out = np.zeros((H*11,W*11,C))
  img_means = np.mean(image, axis=(2))
  tile_size = 20
  for i in range(0,H//2):
    for j in range(0,W//2):
      window = img_means[i*2:i*2+2, j*2:j*2+2]
      tile_id = closestWindow( window )
      del window
      out[i*tile_size:(i+1)*tile_size, j*tile_size:(j+1)*tile_size, :] = tile_imgs[tile_id]
  del img_means
  return out
import gc
gc.collect()

for i in range(0,len(file_list)):
  img = openImage(i)
  print(file_list[i])
  img1 = MosaicTileEffectPic(img)
  saveImage(img1, i)
  del img
  del img1
  gc.collect()
  print(i, '/', len(file_list), 'done')

