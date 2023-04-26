import torch
from pathlib import Path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
from skimage.transform import resize
import seaborn as sns
import cv2

#model weight location: C:\Users\doguk\yolov5\runs\train\my_tree_detector2\weights
model = torch.hub.load("ultralytics/yolov5", "custom", model="C:/Users/doguk/yolov5/runs/train/my_tree_detector2/weights/best.pt")

def DetectTrees(imagePath):
    #Perform inference
    results = model(imagePath)
    return results.xyxy[0].numpy()

def CreateDensityMap(treeCoords, imageShape):
    #Perform kernel density estimation
    kde = sns.kdeplot(treeCoords[:, 0], treeCoords[:, 1], cmap="viridis", shade=True, bw_adjust=0.5)
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
image_path = "C:/Users/doguk/Downloads/DataSet/Tree_counting/test/images/image1.jpg"
detections = DetectTrees(image_path)
tree_count = len(detections)
print(f"Tree count: {tree_count}")

density_map = CreateDensityMap(detections[:, :2], Image.open(image_path).size)
result_image = VisualizeResults(image_path, detections)

#Save and display the images
plt.imsave("C:/Users/doguk/Downloads/DataSet/Tree_counting/output/density_map.png", density_map)
plt.imsave("C:/Users/doguk/Downloads/DataSet/Tree_counting/output/result_image.png", result_image[..., ::-1])

