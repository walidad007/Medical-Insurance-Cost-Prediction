<h1 align="center">Medical Insurance Cost Prediction</h1>


![screencapture-127-0-0-1-8050-2024-06-29-10_33_59](https://github.com/walidad007/Medical-Insurance-Cost-Prediction/assets/122018653/688a2464-3394-43f5-964d-7b4ae5a9b722)

______________________________________________________________________________________________

This project involves predicting medical insurance costs based on various features such as age, sex, BMI, number of children, smoking status, and region. The dataset used for this project is the "insurance.csv" file, which contains 1,338 rows and 7 columns.
______________________________________________________________________________________________

### Table of Contents
* Installation
* Dataset Description
* Exploratory Data Analysis (EDA)
* Preprocessing
* Modeling
* Evaluation
* Usage
* Contributing
* License
______________________________________________________________________________________________

### Installation

To get started with this project, clone the repository and install the necessary packages:

![image](https://github.com/walidad007/Medical-Insurance-Cost-Prediction/assets/122018653/1e2743e5-080a-4f36-b6da-8ee977319dba)
______________________________________________________________________________________________

Ensure you have the following dependencies installed:

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* joblib
* dash
______________________________________________________________________________________________
  
## Dataset Description

The dataset used in this project is insurance.csv. It contains the following columns:

* **age**: Age of the primary beneficiary
* **sex**: Gender of the primary beneficiary (male/female)
* **bmi**: Body mass index
* **children**: Number of children/dependents covered by the insurance
* **smoker**: Smoking status of the beneficiary (yes/no)
* **region**: Residential area of the beneficiary (northwest, southeast, southwest, northeast)
* **charges**: Medical insurance costs billed by the insurance company
______________________________________________________________________________________________

## Exploratory Data Analysis (EDA)

Several plots were generated to understand the distribution of numerical features and the relationship between different variables:

* Histplot for age, BMI, charges, and children.
* Count plots for categorical features (sex, smoker, region).
* Joint plots and scatter plots to visualize relationships between features.
* Box plots and violin plots for distribution analysis.
* Facegrid plots for distribution of four regions analysis.
* Heatmap plot for correlation of all features with one another also with targeted feature.
  
### Example Plots

![image](https://github.com/walidad007/Medical-Insurance-Cost-Prediction/assets/122018653/bbd78cfd-1f45-4132-bea5-a5cc16215b13)

![image](https://github.com/walidad007/Medical-Insurance-Cost-Prediction/assets/122018653/c0109039-37fa-4734-8539-5e3fd0319cb6)

![image](https://github.com/walidad007/Medical-Insurance-Cost-Prediction/assets/122018653/179391d2-9710-4ab5-a181-638127b3eb40)

![image](https://github.com/walidad007/Medical-Insurance-Cost-Prediction/assets/122018653/82b8a3ee-3867-44de-bb61-90cefffc5294)

![image](https://github.com/walidad007/Medical-Insurance-Cost-Prediction/assets/122018653/cc4d5b13-0e54-4428-b9f0-2312d02f989c)

![image](https://github.com/walidad007/Medical-Insurance-Cost-Prediction/assets/122018653/b4588ab2-a4cd-4f2e-8547-0136a02accf4)

![image](https://github.com/walidad007/Medical-Insurance-Cost-Prediction/assets/122018653/a93b6840-bc1f-4279-adec-354742dfd1af)



______________________________________________________________________________________________

## Preprocessing

### Handling Missing Values
The dataset was checked for missing values, and none were found.

### Handling Duplicates
Duplicate rows were removed from the dataset.

### Outlier Treatment
Outliers in the BMI column were capped using the IQR method.

### Encoding Categorical Features
Categorical features (sex, smoker, region) were encoded using one-hot encoding.

### Feature Scaling
Numerical features (age, BMI, children, charges) were standardized using StandardScaler.

### Modeling
Various regression models were trained and evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

The Gradient Boosting Regressor was selected as the final model due to its superior performance.

### Evaluation

The model was evaluated using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R2 score.

* **MSE**: 0.1317
  
* **RMSE**: 0.3629

* **R2 Score**: 0.89


### Model Ranking

Models were ranked based on their performance (lower values are better):

1. Gradient Boosting Regressor: 0.1317
2. Random Forest Regressor: 0.1526
3. Decision Tree Regressor: 0.3288
4. Linear Regression: 0.2418

## Usage
### Running the Dash Application
To run the Dash application for predicting medical insurance costs, execute the following command:

![image](https://github.com/walidad007/Medical-Insurance-Cost-Prediction/assets/122018653/231808da-7edc-4563-bdee-71f2378a6a94)

______________________________________________________________________________________________
### Example Prediction

The Dash application allows users to input the following features:

* Age
* Sex
* BMI
* Number of children
* Smoker status
* Region

Upon clicking the "Predict Price" button, the application will display the predicted medical insurance cost.

______________________________________________________________________________________________
### Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements.
______________________________________________________________________________________________
### License
This project is licensed under the MIT License.

______________________________________________________________________________________________
Feel free to adjust the content as needed for your specific project details and repository structure.
