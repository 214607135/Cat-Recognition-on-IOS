# Cat-Recognition-on-IOS

# Result shown
We successfully build an IOS app, which can detect 17 kinds of different cat breeds with about 50% accuracy.
[App UI](Read_me_pictures/App UI.png)

# Usage notice

The "object_detection" file is all copied from https://github.com/tensorflow/models, please follow the steps in it to learn how to implement this project.

If you want to successfully run our model, you have to download and install all necessary system environments, which is also mentioned in https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md.

Our final exported model in TestModel folder is trained with 25k steps, and the learning rate is 0.001 while batch size is 8. It can detect 17 kinds of cat breeds but the average accuracy is only 52.31%. The pre-trained model we used is ssd_v1_mobilenet_coco.

# Detailed introduction of process for data collecting, model training and cloud deploying

Although there are a lot of similar explaination of model training, I will still try to explain it again, which can also help me to revise the workflow of it. Hope it help :)

### Data collecting and labelling

There are some python files in our **data pre-process** folder, and their function is fully described by their names.
All you need to do is using these files to crawl your favourite data and pre-process them (if you want to train your own model)

After collecting and processing, we used [**labelIMG**](https://github.com/tzutalin/labelImg) to label our images one by one.

After labelling, we used xml_to_csv and csv_to_TFRecord, which convert all label files(xml files) to TFRecord files.

**One more thing**, when use xml_to_csv.py, all xml files should in a folder called **images/train(test)**, then it will generate two csv files in your current directory.

Then **change the label name in csv_to_TFRecord.py file to match yours** before running csv_to_TFRecord by typing the command, which is [here](https://towardsdatascience.com/creating-your-own-object-detector-ad69dda69c85).

### Model training

This is a large part. A lot of preparations need to be done before training the model and it is the most time-consuming task.

I cannot tell how to set your environment, it depends on CPU, GPU or TPU you want to use.

Assume we get ready for the environment:) then we can follow the steps to train our own model **locally**. It is very elaborated.

1. Generate your own label map, same as **Creating a label map** in that tutorial.

2. Download the pre-trained model file in [model zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md), and change the places that need to be modified.(I met a lot of problems in using ssd_fpn model and I still don't know why, hope you won't)

3. Use **_model_main.py_** or **_train.py_** to train the model.
  
  **_model_main.py_:** It is the combination of _train.py_ and _eval.py_, but it will not show the every step of your training process, so you have to use tensorboard to see what happens.
  
  **_train.py_:** It will show every step's detail loss, but it do not contain evaluate process, so you have to open one more terminal and use **_eval.py_**.(But I cannot do that because of the limitation of my GPU)

4. Export the inference_graph
 
If you just want to test the performance of your model, you can just type the command in that tutorial. But if you want to place it in the google cloud platform and build an mobile app, you have to type
  ```python
  python export_inference_graph.py --input_type encoded_image_string_tensor --pipeline_config_path YOUR_TRAINING_FOLDER/pipeline.config --trained_checkpoint_prefix YOUR_TRAINING_FOLDER/model.ckpt-XXXX --output_directory inference_graph/
  ```
5. Test your model locally

It's easy to test the performance of our model locally. Simply use the **_object_detection_tutorial.ipynb_** file in **object_detection** folder, delete the part that download the model online since we are gonna use our own model.
 
### Google Cloud Platform and Firebase
We build our mobile app by placing our model on google server.

1. **Google Cloud Platform init**

Create a project in Google Cloud Platform, then create a bucket and create a folder called **model** in it. Finally put your **saved_model.pb** file in it.

2. **Deploy model**

Follow the instructions [here](https://cloud.google.com/storage/docs/gsutil_install#mac) to init your gcloud command.

Type code: ``` gcloud ml-engine models create MODEL_NAME(whatever) ```

Show the models list: ``` gcloud ml-engine models list ```

Type code: ``` gcloud ml-engine versions create v1 --model=MODEL_NAME --origin=gs://BUCKET_NAME/model --runtime-version=1.12(tensorflow_running_version) ```

3. **Open Firebase**

Open Firebase and create a project, which can be linked to your google cloud platform.

4. **Deploy Cloud Function**

Install [nvm](https://github.com/nvm-sh/nvm/blob/master/README.md)

Install [Firebase CLI](https://firebase.google.com/docs/cli/)

Download **firebase** folder from this project

Run ``` npm install ``` in **firebase/functions/** directory

Update **name** in **params** in index.js: 
```python
name: 'projects/your-project-name/models/your-model-name'
```

Run ``` firebase deploy --only functions ```

If succeed, you can see there is a function in your Firebase.

5. **Test Firebase**

Create a folder called **images** in storage in Firebase

upload an image to it. Then check if the prediction is shown in Firebase database. You can also check the function log to see why it's not successful.
[Firebase database](Read_me_pictures/Firebase database.png)

