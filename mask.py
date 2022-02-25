# Object to 255, backgroud to 0
from glob import glob
import numpy as np 
import json 
import os 
import cv2 
import matplotlib.pyplot as plt
from numpy.lib.function_base import append

# Image path
image_path = 'NA_datasets/'

# Json path
json_path = "json_datasets/"
json_paths = glob(os.path.join(json_path, "*.json"))

# Read each json path
for json_path in json_paths:
    with open(json_path) as f:
        imgs_anns = json.load(f)

    # Read file name from "imagePath"
    file_name = os.path.join(image_path, imgs_anns["imagePath"])
    
    # Read image
    image = cv2.imread(file_name)

    # Get image name
    image_name = file_name.split("\\")

    # Get point label
    points = imgs_anns["shapes"]

    image_out = np.zeros_like(image)
    # print(points)
    for p in points:
        # Polygon corner points coordinates
        pts = np.array(p['points'],np.int32)
        pts = pts.reshape((-1, 1, 2))

        mask = np.zeros((images.shape[0], images.shape[1]))

        cv2.fillConvexPoly(mask, pts, 1)
        
        mask = mask.astype(np.bool)
        
        # Object to 255
        image_out[mask] = 255

    # print(image_out.shape)
    cv2.imwrite(f'GT_datasets/{image_name[-1]}', image_out)




    
