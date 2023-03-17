#Imports 
#import os
import os
import random
import matplotlib.pyplot as plt
from PIL import Image

#Load of datasets
images_dir = r'C:\Users\sanje\OneDrive\Desktop\Seg-Class\Dataset\images'
segmaps_dir = r'C:\Users\sanje\OneDrive\Desktop\Seg-Class\Dataset\segmaps'

fns = os.listdir(images_dir)
fns = [fn.split('.')[0] for fn in fns]

fig, axes = plt.subplots(3, 2, figsize=(16, 8))
axes = axes.ravel()
for ax in axes:
    ax.axis('off')
for i in range(0, 6, 2):
    fn = f'{random.sample(fns, 1)[0]}.png'
    image = Image.open(os.path.join(images_dir, fn))
    segmap = Image.open(os.path.join(segmaps_dir, fn))
    axes[i].imshow(image)
    axes[i+1].matshow(segmap, cmap='tab20')
plt.show()
