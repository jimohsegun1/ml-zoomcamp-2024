# ML Zoomcamp Mid-term project 2024
|![](Images/heartimg.jpg)|
|:--:|
|*[Image from https://unsplash.com](https://media.istockphoto.com/id/1359314170/photo/heart-attack-and-heart-disease-3d-illustration.webp?a=1&b=1&s=612x612&w=0&k=20&c=Gx3upq3O3QK8_B3KW7j5MIdWzm7HkdFyUN2RPjt5Olo=)*|

## Problem Description
The used dataset is from [Kaggle](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset/data).
The csv file is quite small so I put it in the Data folder.
It is a Heart Attack Analysis & Prediction Dataset for heart attack classification.
The dataset has 14 columns and we can use the "output" column as our target variable. This column devide the patients in patients with less chance of heart attack (output = 0) and patients with more chance of heart attack (output = 1). 

The Dataset contains multiple columns
| Column name | Description |
| ----------- | ----------- |
| age | Age of the patient  |
| sex | Sex of the patient  |
|     |   Value 0: female   |
|     |   Value 1: male     |
| cp  | Chest Pain type     |
|     |   Value 1: typical angina |
|     |   Value 2: atypical angina |
|     |   Value 3: non-angina pain |
|     |   Value 4: asymptomatic |
| trtbps |    resting blood pressure (in mm Hg) |
| chol   |   cholestoral in mg/dl fetched via BMI sensor |
| fbs    |   (fasting blood sugar > 120 mg/dl) |
|     |   Value 1: true |
|     |   Value 0: false |
| restecg |	resting electrocardiographic results |
|     |   Value 0: normal |
|     |   Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) |
|     |   Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria |
| thalachh |  maximum heart rate achieved |
| exng  |    exercise induced angina |
|     |           Value 1: yes |
|     |           Value 0: no |
| oldpeak |   ST depression induced by exercise relative to rest (‘ST’ relates to positions on the ECG plot.) |
| slp     |  the slope of the peak exercise ST segment |
|     |           Value 0: downsloping |
|     |           Value 1: flat |
|     |           Value 2: upsloping |
| caa |      number of major vessels (0-3) |
| thall |    A blood disorder called thalassemia Value 0: NULL (dropped from the dataset previously |
|     |   Value 1: fixed defect (no blood flow in some part of the heart) |
|     |   Value 2: normal blood flow |
|     |   Value 3: reversible defect (a blood flow is observed but it is not normal) |
| output |   target --> 0 = less chance of heart attack; 1 = more chance of heart attack |

| id | age | sex | cp | trtbps | chol | fbs | restecg | thalachh | exng | oldpeak | slp | caa | thall |	output |
|-|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 0 | 63 | 1 | 3 | 145 | 233 | 1 | 0 | 150 | 0 | 2.3 | 0 | 0 | 1 | 1 |
| 1 | 37 | 1 | 2 | 130 | 250 | 0 | 1 | 187 | 0 | 3.5 | 0 | 0 | 2 | 1 |
| 2 | 41 | 0 | 1 | 130 | 204 | 0 | 0 | 172 | 0 | 1.4 | 2 | 0 | 2 | 1 |
| 3 | 56 | 1 | 1 | 120 | 236 | 0 | 1 | 178 | 0 | 0.8 | 2 | 0 | 2 | 1 |
| 4 | 57 | 0 | 0 | 120 | 354 | 0 | 1 | 163 | 1 | 0.6 | 2 | 0 | 2 | 1 |

This project provides a model to predict this value. 
There is a notebook (/Notebook/notebook.ipynb) that contains:
- data preparation 
- EDA
- feature importance analysis
- Training of multiple models
- Tuning of multiple models 
- Selecting the best model

The model is provided as containerized web service that listens on port 9797.

## Reproducibility
It's convenient to track my progress using the Makefile, which provides all the necessary commands:
1. To set up the environment, use "make environment" or follow the listed commands.
2. Inspect the Jupyter notebook in the Notebook folder.
3. Start model training of the final model with "make train", saving it in the Model folder.
4. Deploy the web server in a Docker container listening on port 9797 with "make deploy".
5. Test the deployment with "make test_deploy" using a sample patient record.

Additional commands for managing the environment:
- "make stop_docker" to halt running Docker containers.
- "make clean" for environment cleanup
- "make deactivate_environment" to deactivate the environment in the current terminal (in case I forget about the "deactivate" command)