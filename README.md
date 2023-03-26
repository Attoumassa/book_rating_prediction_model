# Book Rating regression project 

## 1. Project Description

This is an important component of your project that many new developers often overlook.

Your description is an extremely important aspect of your project. A well-crafted description allows you to show off your work to other developers as well as potential employers.

The quality of a README description often differentiates a good project from a bad project. A good one takes advantage of the opportunity to explain and showcase:

- What your application does,
- Why you used the technologies you used,
- Some of the challenges you faced and features - you hope to implement in the future.

## 2. How to Install and Run the Project


The project requires the following to be installed. 
- [python3.9](https://www.python.org/downloads/)
- [git](https://git-scm.com/)

Optionally, for easier virtual environment creation:
- [anaconda](https://www.anaconda.com/)

#### Instructions

Clone the repository:
```shell
git clone https://github.com/Attoumassa/book_rating_prediction_model.git
cd book_rating_prediction_model
git checkout main
```

Create and activate python virtual environment:

- Using conda (preferred method)
```shell
conda create -n "book_rating_prediction_model_env_aamv" python=3.9
conda activate book_rating_prediction_model_env_aamv
```

- Using venv
```shell
# Create the virtual environment
python3.9 -m venv book_rating_prediction_model_env_aamv

# Activate the virtual environment
## UNIX-like systems
source book_rating_prediction_model_env_aamv/bin/activate

## Windows with powershell
.\book_rating_prediction_model_env_aamv\Scripts\Activate.ps1
```

Installing package dependencies
```shell
pip install -r requirements.txt
```

**Open the notebook:**

```shell
jupyter notebook src/final_notebook.ipynb
```

**Open the report:**

```shell
cd report
python report/report.py
streamlit run report/report.py
```



## 3. How to Use the Project

The project consists of a jupyter notebook. simply run each cell and read the comments. 

The project is structured as follow:

- Introduction

- Data exploration
    - Loading the data
    - Preliminary analysis
    - Removing unused data

- Feature Engineering
    - Publication date
    - Language
    - Title, publisher and author data
    - Outliers
    - Conclusion
- Data modeling
    - Splitting the data
    - How to evaluate a model
    - Linear Regression
    - Random Forest
    - Decision Tree Regressor
    - Support Vector Regression (SVR) with Radial Basis Function (RBF) kernel
    - Gradient Boosting
    - Adaboost
    - Stacking

- Comparing the models
    - Modeling score comparison
    - Comparing model with all features vs less features
    - Comparing with and without outliers

- Conclusion

Provide instructions and examples so users/contributors can use the project. This will make it easy for them in case they encounter a problem – they will always have a place to reference what is expected.

You can also make use of visual aids by including materials like screenshots to show examples of the running project and also the structure and design principles used in your project.

Also if your project will require authentication like passwords or usernames, this is a good section to include the credentials.

## 4. Credits

This project has been made by:
- [Attoumassa Samaké](https://github.com/Attoumassa)
- [Marguerite Nken](https://github.com/marguerite-nken)
- [Vixra Keo](https://github.com/Vixk2021)
- [Antoine Bedouch](https://github.com/Antoine-bdc)