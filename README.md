# Cat-Recognition-on-IOS

# Usage notice
The "object_detection" file is all copied from https://github.com/tensorflow/models, please follow the steps in it to learn how to implement this project.

If you want to successfully run our model, you have to download and install all necessary system environments, which is also mentioned in https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md.

Our final exported model in TestModel folder is trained with 25k steps, and the learning rate is 0.001 while batch size is 8. It can detect 17 kinds of cat breeds but the average accuracy is only 52.31%. The pre-trained model we used is ssd_v1_mobilenet_coco.

# Detailed introduction of process for data collecting, model training and cloud deploying
Although there are a lot of similar explaination of model training, I will still try to explain it again, which can also help me to revise the workflow of it. Hope it help :)

### Data collecting
