# Face Presentation Attack Detection 



## Introduction

Currently, with the advancement of technology, security systems that use facial recognition are becoming increasingly common and, at the same time, increasingly vulnerable. As the years go by, more sophisticated techniques for bypassing facial recognition systems are emerging, such as the use of 3D facial masks (made of silicone, gel, among other materials), the use of deep fakes, as well as the use of more classic techniques, like taking a photo or recording a video from a cell phone or computer screen that contains the target's image. With the improvement in camera quality and screen resolution, these become stronger attacks over time.

An attempted fraud is called a presentation attack, or also a spoof attack. Face PAD systems are security systems with the goal of identifying whether a video or an image that arrives at the system is real (captured by the individual themselves), or an attempt at fraud, such as when someone tries to take a photo of a photo of the target (photo attack), or record a video of an existing video of the target (replay attack), using 3D masks, deep fakes, or merely placing a photo of the target in front of their face.

This is a task that presents many challenges in the present times, as there are many different types of attacks, and developing techniques that can generalize well is a challenge that is currently greatly engaging the academic community.

## Tech Stack Description

This project presents the following container:

* FastAPI: Requests via API
    * Image: 0.95.0
    * Database Port: 8000

## File Structure

```bash
desafio-01/
|---- README.md
|---- Dockerfile
|---- requirements.txt
|---- app.py (FastAPI code)
|---- src/
      |---- model.py (model definition)
      |---- train.py (model training script)
      |---- utils.py (helper functions)
|---- data/
|---- model/
      |---- model.h5 (trained model 1)      
|---- notebooks/
      |---- fpad.ipynb
|---- run.sh
```

## Dataset

This project uses the CelebA dataset. Due to its size, the dataset is not included in the repository. Here's how to prepare the data for this project:

1. Download the CelebA dataset from 'https://mostqi-infra-sp-public.s3.sa-east-1.amazonaws.com/desafios/MLChallenge_Dataset.zip'
2. Unzip the downloaded file. This should result in a directory structure like the following:
    ```
    MLChallenge_Dataset/
                        data/
                            1/   
                                live/
                                    image1.jpg
                                    image2.jpg
                                    image3.jpg
                                spoof/
                                    image1.jpg
                                    image2.jpg
                                    image3.jpg
                            2/
                            ...
    ```
3. Move the `data/` subfolder into the `data/` directory in the root of this repository.

4. Due to Github storage contraints, you have 2 options to build the model. You can you the notebook included and run the specific cell to make it and then import it to the folder 'model' inside the root. The second option in to run the script inside 'scripts' folder which will run the necessary .py files to build the model. One must notice that, after building the model, you should delete it to avoid conflicts while trying to commit to the repository.


## Setup

### Requirements
    
    $ Must have Docker installed in your machine. Ignore it if using CDE (Cloud Development Environment), i.e., Gitpod, GitHub Codespaces, etc

### Clone project

    $ git clone https://github.com/fernandodgl/fpad-challenge

### Build containers

Inside the 'FPAD-CHALLENGE/desafios-ml/desafio-01' folder (root)

    $ chmod +x run.sh

### Start containers

At the same path above:

    $ ./run.sh

### Check if you can access:

|        Application        |URL                          |Credentials                         |
|----------------|-------------------------------|-----------------------------|    
|FastAPI | [http://localhost:8000/docs](http://localhost:8000/docs)|  |         |
  

## References

https://arxiv.org/pdf/2305.09285.pdf

https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9925105

https://www.researchgate.net/figure/comparing-cIOU-of-VGG-16-DenseNet121-and-ResNet50-for-a1D1595-while_fig23_330713580

https://openaccess.thecvf.com/content/WACV2021/papers/Zhang_ResNet_or_DenseNet_Introducing_Dense_Shortcuts_to_ResNet_WACV_2021_paper.pdf

https://microscope.openai.com/models/resnetv2_50_slim?models.technique=deep_dream

[CelebA-Spoof Repo](https://github.com/ZhangYuanhan-AI/CelebA-Spoof)
