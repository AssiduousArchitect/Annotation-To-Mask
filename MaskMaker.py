######################################
##  JERIN PAUL MATHEW - 05 NOV 2018 ##
######################################

"""
MaskMaker.py extracts coordinates of rooftops from a JSON file and outputs Masked Images of all the Roofs.
"""

import json
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source', help = 'Full path of the JSON file.', default='bounds.json')
parser.add_argument('--output', help = 'Full path of the Directory where MASKS will be exported.', default='./Masks/')
args = parser.parse_args()

path = args.source
destination = args.output + '/'

if not os.path.exists(path):
	print(path, "does not exist.")
	exit()

with open(path) as json_data:	
	d = json.load(json_data)

if not os.path.isdir(destination):
    os.mkdir(destination)
    

for im in d.keys():
    image = Image.new("RGB", (300, 300))
    filename = d[im]['filename']
    draw = ImageDraw.Draw(image)
    
    roofs = d[im]['regions'] 
    
    for roof in roofs:
        roof_data = [coords for coords in zip(roof['shape_attributes']['all_points_x'], roof['shape_attributes']['all_points_y'])]
        draw.polygon(roof_data, fill="white")
    print("Exporting MASK for " + filename)
    image.save(destination + filename)

print("All MASKS were successfully exported.")	
