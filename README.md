
# Object Detection and Segmentation using Python Libraries






## Introduction

We have built an end-to-end pipeline for Image Detection and Segmentation using the best
industry practices. The segmentation model has been provided with a UI to run predictions and
further was dockerized and deployed on the cloud.

Object detection is a task in computer vision that identifies the presence and type of one or more objects in a given image. Here we build a
bounding box corresponding to each class in the image.

Image segmentation is grouping together the pixels that have similar attributes. It can be
considered as the next step to object detection. Image segmentation creates a
pixel-wise mask for each object in the image. This technique gives us a far more granular
understanding of the object(s) in the image and tells us about the shape of the object.

![](Object%20Detection%20and%20Segmentation%20image.jpeg)

Image segmentation is transforming industries with applications such as Traffic Control
Systems, Self Driving Cars, and Locating objects in satellite images. Some of the popular image
segmentation algorithms are region-based, edge-based, cluster-based, MRCNN etc.

We can broadly divide image segmentation techniques into two types: semantic and instance.
Semantic segmentation treats multiple objects of the same class as a single entity. On the other
hand, instance segmentation treats multiple objects of the same class as distinct individual
objects (or instances).

![](Semantic%20vs%20Instance%20Segmentation%20image.jpeg)



## Algorithm

● We use PointRend algorithm (published on 2019) based on MRCNN. MRCNN works on constant resolution on images whereas PointRend works on different level of resolution.

● It starts with low resolution images which helps in efficiency and then keeps on increasing the resolution to only predict points that are uncertain and hence increasing the accuracy.

● It can be compared to boosting algorithms seeking to improve the prediction power by training a sequence of weak models, each compensating the weaknesses of its predecessors.
## UI

● Streamlit is an open-source python framework for building web apps for Machine Learning and Data Science.

● We have provided 3 ways to run image segmentation - upload image, webcam capture and pre-uploaded examples.


## Containerization

Docker is a software platform that allows you to build, test, and deploy applications quickly. Docker packages software into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime. Using Docker, you can quickly deploy and scale applications into any environment and know your code will run.
## Deployment

We deployed our application on multiple cloud platforms such as Heroku, Google Cloud Platform and Streamlit Cloud. The docker image was pushed into the artifactory/container registry of respective cloud platforms and then deployed.
