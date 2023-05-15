Version 0.1
The main program uses a lot of folder directories.
Please check related directories and change them with suitable ones in your environment.
*******************
model weights: your trained location
example: "C:\Users\doguk\yolov5\runs\train\my_tree_detector2\weights"
*******************
test inputs: where is your dataset
example: "C:\Users\doguk\Downloads\DataSet\Tree_counting\test\images\image1.jpg"
attention (ver0.1): program can only take one image per cycle. You have to change location if you want to test different image.
*******************
output locations: where will the output images be created
example: C:\Users\doguk\Downloads\DataSet\Tree_counting\output

version 0.1.1
First pretrained model weight added.
Sample train prompt:
python train.py --img 640 --batch 16 --epochs 100 --data C:\Users\doguk\Downloads\DataSet\Tree_counting\data.yaml --cfg yolov5s.yaml --weights yolov5s.pt --name my_tree_detector

version 0.1.2
requirements file must be with the same filepath with main.py
first executable version

version 0.1.4
in this version you will give your test image location via console.
train and validation image paths and weight path hierarchically reorganized.
 
version 0.1.5
Density mapping render attribute error fixed.
Scatter plotting added.
Some minor fixes.
Started to work on brand-new dataset.
Sample Train Prompt:
python train.py --img 640 --batch 16 --epochs 100 --data C:\Users\doguk\Downloads\Tree_counting1\data.yaml --cfg yolov5m.yaml --weights yolov5m.pt --name Tree_weight_dataset_1

version 0.1.6
New weight added.

version 0.1.7
Most accurate and fast moving weight so far has been added.