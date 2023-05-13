import torch
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
from skimage.transform import resize
import seaborn as sns
import cv2
import os
import sys

os.environ['KMP_DUPLICATE_LIB_OK']='True'

yoloPath = "yolov5"
modelPath = "models/best.pt"
if modelPath == None:
    print('Model cannot be found')
model = torch.hub.load(yoloPath, "custom", path=modelPath, force_reload=True,source='local')

def DetectTrees(imagePath):
    #Perform inference
    results = model(imagePath)
    return results.xyxy[0].numpy()

def CreateDensityMap(treeCoords, imageShape):
    x, y = treeCoords[:, 0], treeCoords[:, 1]
    data = np.column_stack((x, y))
    #Perform kernel density estimation
    kde = sns.kdeplot(data=data, fill=True, bw_adjust=0.5)
    density_map = np.array(kde.get_figure().canvas.renderer.buffer_rgba())[:, :, :3]

    #Resize the density map to match the input image shape
    density_map = resize(density_map, (imageShape[0], imageShape[1]), anti_aliasing=True, mode="reflect")

    plt.clf()
    return density_map

def VisualizeResults(image_path, detections):
    image = cv2.imread(image_path)

    for *xyxy, conf, cls in detections:
        label = model.names[int(cls)]

        #Draw bounding box
        cv2.rectangle(image, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (255, 0, 0), 2)
        cv2.putText(image, label, (int(xyxy[0]), int(xyxy[1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    return image

#image output path: C:\Users\doguk\Downloads\DataSet\Tree_counting\output
#image test path: C:\Users\doguk\Downloads\DataSet\Tree_counting\test\images
#it takes only one image for now.
image_path = input('Give imagePath:')
#image_path = "Dataset/train/images/bp_262118_4_174541_4_19_jpg.rf.4f13d4f2edf6e474d53229cd1ca76b56.jpg"
detections = DetectTrees(image_path)
tree_count = len(detections)
print(f"Tree count: {tree_count}")

density_map = CreateDensityMap(detections[:, :2], Image.open(image_path).size)
result_image = VisualizeResults(image_path, detections)

#Save and display the images
plt.imsave("output/density_map.png", density_map)
plt.imsave("output/result_image.png", result_image[..., ::-1])