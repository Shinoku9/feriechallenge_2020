from PIL import Image
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
new_dir_path = r'D:\Python_nauka\Ferie_challenge\Smaller'

extensions = ('.tif','.tiff','.bmp','.jpg','jpeg','.gif','.png','.eps','.raw','.cr2','.nef','.orf','.sr2')

arr = []
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(extensions):
            arr.append(file)

if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)

arr_len = len(arr)

for x in range (0, len(arr)):
    img = Image.open(arr[x])
    (width, height) = (img.width//2, img.height//2)
    img_resized = img.resize((width,height))
    img_resized.save(r'D:\Python_nauka\Ferie_challenge\Smaller\%s' %(arr[x]))
