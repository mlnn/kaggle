#mount google
from google.colab import drive
drive.mount('/content/drive')

#Runtime->Change runtime type->GPU or TPU
#check it
import tensorflow as tf
tf.test.gpu_device_name()

# kaggle in colab - upload json from kaggle API
from google.colab import files
files.upload()

# Let's make sure the kaggle.json file is present.
!ls -lha kaggle.json
# Next, install the Kaggle API client.
!pip install -q kaggle
# The Kaggle API client expects this file to be in ~/.kaggle,
# so move it there.
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
# This permissions change avoids a warning on Kaggle tool startup.
!chmod 600 ~/.kaggle/kaggle.json

!kaggle competitions download -c rsna-pneumonia-detection-challenge

import os
import zipfile

!mkdir stage_2_test_images
!mkdir stage_2_train_images

!mv stage_2_train_images.zip stage_2_train_images
!mv stage_2_test_images.zip stage_2_test_images

os.chdir('stage_2_test_images')

for file in os.listdir():
  if file.endswith('zip'):
    zip_ref = zipfile.ZipFile(file, 'r')
    zip_ref.extractall()
    zip_ref.close()
    
os.chdir('../stage_2_train_images')

for file in os.listdir():
  if file.endswith('zip'):
    zip_ref = zipfile.ZipFile(file, 'r')
    zip_ref.extractall()
    zip_ref.close()

os.chdir('..')

for file in os.listdir():
  if file.endswith('zip'):
    zip_ref = zipfile.ZipFile(file, 'r')
    zip_ref.extractall()
    zip_ref.close()
