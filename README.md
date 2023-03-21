# Predicting your geological sample using CNN
This machine learning web-application was built based on a small dataset (1000 pictures, 
with 5 categories: amethyst, ammonite, aventurin, empty, obsidian), and its purpose is to recognize minerals and fossils from a personal collection.


## Usage

Open a new terminal:

1.Go to your Downloads location (`cd Downloads`)

2.Clone this repository (`git_clone git@github.com:IonelS-coder/predict_geological_sample.git`)

3.Open the predict_geological_sample folder (`cd predict_geological_sample`)

4.Install the necessary libraries (ideally in a newly created conda environment:

4.1 Create and activate the conda environment
 `conda create -n predict_geological_sample pip python=3.8`
 `conda activate predict_geological_sample`
 `pip install -r requirements.txt`

5.Check that all the necessary libraries were installed (`pip list`)

6.Access streamlit folder (`cd streamlit`) and run this command:
        - `streamlit run interactive_app_rocks.py`
        - open the link (e.g. http://localhost:8501/) in a browser.
        - load one of the test images and check the results

Test and have fun with the app.


** Extra
For more details check the following Jupyter Notebook file* (*jupyter package is required): `M3_TEST_Rock_mineral_image_classification_transfer_learning.ipynb` 

Check also the `M3_presentation.slides.html` file from the reveals.js folder for a presentation of the project

