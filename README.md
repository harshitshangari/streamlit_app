# Forest Cover Type Prediction EDA using Streamlit App
This Streamlit app provides an Exploratory Data Analysis (EDA) of the Forest Cover Type Prediction dataset available in Kaggle. It allows users to explore and visualize various aspects of the dataset, including statistical description of features, correlation heatmaps, distribution plots, scatter plots and violin plots.

## Installation

To run this app, you'll need following Python libraries installed:

- pandas
- streamlit
- numpy
- seaborn
- matplotlib

You can install these requirements using:
```
pip3 install -r requirements.txt
```
## Running the app without Docker

First, clone the github repository.
```
git clone https://github.com/harshitshangari/streamlit_app.git
```
Go to the project directory.
```
cd streamlit_app
```
Run the Streamlit app.
```
streamlit run app.py
```

## Running the app with Docker
First, clone the github repository.
```
git clone https://github.com/harshitshangari/streamlit_app.git
```
Go to the project directory.
```
cd streamlit_app
```
Build the Docker image.
```
docker build -t streamlit .
```
Run the Docker container.
```
docker run -p 8501:8501 streamlit
```
The app will then be accessible through http://localhost:8501

## Running the app using Dockerhub
You can pull and run the docker image using
```
docker pull harshitshangari/streamlit_fc_app
```
```
docker run -p 8501:8501 harshitshangari/streamlit_fc_app
```
The app will then be accessible through http://localhost:8501

You can rerun the app using the three dots at the top right of the URL in case of any issues.

You can also find my dockerhub repo here:
```
https://hub.docker.com/repository/docker/harshitshangari/streamlit_fc_app/general
```
## Contributing
All content in this repository is licensed under the MIT license.

