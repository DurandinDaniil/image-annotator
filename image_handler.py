import os
import sys
from urllib.request import urlopen
from PIL import Image, ImageFont, ImageDraw 

def image_annotation(path_load, path_save):
    img_paths = os.listdir(path_load)
    for img in img_paths:
        
        #read image 
        image = Image.open(path_load + '/' + img)
        img_width, img_height = image.size
        
        #take first and last name according image name pattern
        first_name, last_name =  img.split('.')[0].split('-')
        
        #create image title 
        title_text = u"\u00A9" + first_name.title() + ' ' + last_name.title()
        
        # count font size depend on the image width 
        font_size = int((img_width + len(title_text))* 0.05)

        #download fonts (taking a time, because of fonts downloading,  
        #it can be executed out of loop, if we dont changing font size)
        font_url = 'https://github.com/DurandinDaniil/image-annotator/blob/main/Roboto-Black.ttf?raw=true'
        font_type = ImageFont.truetype(urlopen(font_url), size = font_size)
        
        # count title size for evaluating coordinates of text
        text_width, text_height = font_type.getsize(title_text)
        
        #make image mutable and insert text
        image_edit = ImageDraw.Draw(image)
        image_edit.text((img_width - text_width - int(font_size/2), img_height -text_height - int(font_size/2)), title_text, (255, 255, 255), font=font_type)
        
        #saving images
        os.makedirs(path_save, exist_ok=True)
        image.save(path_save + '/'+ img )



args = sys.argv

#take paths depend on the arguments quantity
if len(args) == 1:
    print('No path specified')
    sys.exit()
elif len(args) == 2:
    path_load = args[1]
    path_save = './output-images/'
else:
    path_load = args[1]
    path_save = args[2]

image_annotation(path_load, path_save)




