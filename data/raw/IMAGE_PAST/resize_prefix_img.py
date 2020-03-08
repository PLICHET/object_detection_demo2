import glob
from PIL import Image
import os

class_name = 'PASTU'

os.mkdir('resized')
file_list = sorted(glob.glob('*.bmp'))
for idx,file_name in enumerate(file_list):
  im = Image.open(file_name)
  new_width  = 640
  new_height = 480
  im = im.resize((new_width, new_height), Image.ANTIALIAS)
  im.save('resized/' + class_name + '_' + '3' + str(idx+1).zfill(3) + '.jpg')
