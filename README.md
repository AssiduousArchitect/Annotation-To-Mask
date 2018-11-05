# Annotation-To-Mask

MaskMaker.py extracts coordinates of rooftops from a JSON file and outputs Masked Images of all the Roofs.

## Prerequisites

1. Python 3.5.x
2. PIL (Python Imaging Library) - _pip install Pillow_

## How to use.

**Synatx:**  
python **MaskMaker.py** --source \<PATH of JSON file> --output \<PATH for Destination directory.>  

**Default values:**  
--source - *bounds.json*  
--output - *./Masks/*  
Placing this script in the same directory as the json file will create the masks without supplying any arguments.
