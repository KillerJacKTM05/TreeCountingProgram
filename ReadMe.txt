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