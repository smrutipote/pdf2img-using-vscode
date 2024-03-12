import re
import os
import pdf2image
from pdf2image import convert_from_path

pop_path=r'C:\Program Files\poppler-24.02.0\Library\bin'
file_path=r'C:\Users\D\sample.pdf'

folder_name=file_path.split('\\')[-1].split('.')[0]
print(folder_name)

path=os.getcwd()
print(path)

folder_path=os.path.join(path,folder_name)
print(folder_path)
if not os.path.exists(folder_path):
    folder_path=os.mkdir(folder_path)
    print(folder_path)

images=convert_from_path(file_path,dpi=300,poppler_path=pop_path)

for i,image in enumerate(images):
    file_name= folder_path + '\\image_' + str(i) + '.png'
    print(file_name)
    
    image.save(file_name,'PNG')