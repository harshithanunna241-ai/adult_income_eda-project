# Adult Income Data Cleaning, EDA and Machine Learning

## 1. Project Overview

This project analyzes the UCI Adult Income dataset to understand which demographic, education, and work-related characteristics are associated with annual income above USD 50K.

The project includes:

* Data collection
* Data cleaning
* Exploratory Data Analysis (EDA)
* Data visualization
* Machine Learning
* Logistic Regression
* Model evaluation
* Streamlit application for income prediction

---

## 2. Problem Statement

The main objective of this project is to analyze census information and predict whether a person's annual income is:

* `<=50K`
* `>50K`

The project focuses on understanding associations between income and factors such as education, occupation, age, workclass, sex, working hours, and capital-related variables.

---

## 3. Dataset

The dataset used in this project is the **UCI Adult Income Dataset**.

Source:

UCI Machine Learning Repository
https://archive.ics.uci.edu/dataset/2/adult

The combined dataset contains approximately **48,842 records**.

The original dataset contains 14 input features and one income target.

### Main Features

* age
* workclass
* fnlwgt
* education
* education_num
* marital_status
* occupation
* relationship
* race
* sex
* capital_gain
* capital_loss
* hours_per_week
* native_country

### Target

`income`

The target has two categories:

* `<=50K`
* `>50K`

A numerical target called `high_income` was also created:

* `0` = `<=50K`
* `1` = `>50K`

---

## 4. Data Cleaning

The following data-cleaning steps were performed:

1. Combined the original training and testing datasets.
2. Added a `source_split` column.
3. Checked for missing-value markers represented by `?`.
4. Replaced `?` with missing values.
5. Replaced missing `workclass`, `occupation`, and `native_country` values with `Unknown`.
6. Cleaned the income labels.
7. Created the `high_income` target variable.
8. Converted numerical columns to appropriate numeric data types.
9. Created `age_group`.
10. Created `hours_group`.
11. Created `net_capital`.
12. Checked for duplicate records.
13. Saved the cleaned dataset.

---

## 5. Exploratory Data Analysis

The following analyses were performed:

* Income distribution
* Income by education
* Income by occupation
* Income by age group
* Income by workclass
* Income by sex
* Weekly working hours by income
* Working-hour groups by income
* Capital gain and capital loss analysis
* Numerical correlation analysis

### Visualizations

The project generates the following charts:

* Income Distribution
* Income by Education
* Income by Occupation
* Income by Age Group
* Income by Workclass
* Income by Sex
* Weekly Working Hours by Income
* Income by Working-Hour Group
* Correlation Heatmap
* Logistic Regression Confusion Matrix

---

## 6. Machine Learning

A **Logistic Regression** model was developed to predict the `high_income` target.

### Machine Learning Steps

1. Loaded the cleaned dataset.
2. Separated input features and target.
3. Removed target and non-predictive columns.
4. Encoded categorical variables using one-hot encoding.
5. Split the dataset into training and testing data.
6. Applied StandardScaler.
7. Trained Logistic Regression.
8. Generated predictions.
9. Evaluated the model.

### Evaluation Metrics

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 7. Model Files

The trained model files are stored in the `models` folder.

```text
models/
├── income_model.pkl
├── scaler.pkl
└── model_metadata.json
```

### File Description

`income_model.pkl`
Stores the trained Logistic Regression model.

`scaler.pkl`
Stores the StandardScaler used during model training.

`model_metadata.json`
Stores model information and feature names.

---

## 8. Streamlit Application

A Streamlit application is included to provide a user interface for income prediction.

The application allows users to enter information such as:

* Age
* Workclass
* Education
* Education Number
* Marital Status
* Occupation
* Relationship
* Race
* Sex
* Capital Gain
* Capital Loss
* Hours per Week
* Native Country

The application then predicts whether the estimated income is:

```text
<=50K
```

or

```text
>50K
```

---

## 9. Project Structure

```text
adult_income_eda_project/
│
├── README.md
├── requirements.txt
├── app.py
│
├── data/
│   ├── raw/
│   │   ├── adult.data
│   │   ├── adult.test
│   │   └── adult_income_raw.csv
│   │
│   └── cleaned/
│       └── adult_income_cleaned.csv
│
├── reports/
│   ├── tables/
│   ├── charts/
│   ├── EDA_Report.docx
│   └── EDA_Report.pdf
│
├── models/
│   ├── income_model.pkl
│   ├── scaler.pkl
│   └── model_metadata.json
│
└── src/
    ├── Data Cleaning.ipynb
    ├── Data Analysis.ipynb
    ├── ML Model.ipynb
    └── build_pdf_report.py
```

---

## 10. Installation

Clone or download the project and open the project folder in VS Code.

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## 11. Running the Project

### Run the Streamlit Application

From the main project folder:

```bash
python -m streamlit run app.py
```

The application will open in your web browser.

### Run the Notebooks

Open the following notebooks in VS Code or Jupyter:

```text
src/Data Cleaning.ipynb
src/Data Analysis.ipynb
src/ML Model.ipynb
```

Run the notebooks in the order shown above.

### Generate the PDF Report

Run:

```text
src/build_pdf_report.py
```

This generates:

```text
reports/EDA_Report.pdf
```

---

## 12. Results

The project identifies differences in income levels across demographic, education, occupation, work, and capital-related characteristics.

The Logistic Regression model provides a baseline machine-learning approach for predicting whether annual income is above USD 50K.

Model performance is reported using accuracy, precision, recall, F1 score, and a confusion matrix.

---

## 13. Limitations

This project describes associations and does not establish causal relationships.

Important limitations include:

* The dataset is historical.
* Demographic characteristics are included in the dataset.
* The analysis is descriptive.
* The visual summaries are unweighted.
* Model predictions should not be interpreted as guaranteed income outcomes.

---

## 14. Conclusion

This project demonstrates a complete data-science workflow using the UCI Adult Income dataset.

The workflow includes:

```text
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Data Visualization
      ↓
Feature Preparation
      ↓
Logistic Regression
      ↓
Model Evaluation
      ↓
Streamlit Application
```

The project provides practical experience in data preprocessing, exploratory analysis, visualization, machine learning, model evaluation, and deployment using Streamlit.

---

## 15. Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit
* ReportLab
* Jupyter Notebook
* VS Code
