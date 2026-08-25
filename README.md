# 🛍️ Social Network Ads Purchase Prediction

### K-Nearest Neighbors (KNN) | Machine Learning | Streamlit

A Machine Learning project that predicts whether a customer is likely to purchase a product after viewing a social network advertisement.

The project uses the **K-Nearest Neighbors (KNN)** algorithm with feature scaling and provides an interactive prediction interface built using **Streamlit**.

---

## 📌 Project Overview

The goal of this project is to predict customer purchase behavior based on demographic and salary information.

The model uses the following features:

* Gender
* Age
* Estimated Salary

The numerical features are scaled using **StandardScaler** before applying the KNN algorithm.

The model predicts one of two outcomes:

* `0` → Not Purchased
* `1` → Purchased

The trained KNN model and scaler are saved as `.pkl` files and used by the Streamlit application.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Analyze customer purchase behavior.
* Perform data preprocessing.
* Apply feature scaling.
* Build a K-Nearest Neighbors classification model.
* Compare KNN performance with and without scaling.
* Evaluate model performance.
* Save the trained model using Pickle.
* Build an interactive Streamlit application.
* Make real-time purchase predictions.

---

## 🚀 Key Features

* ✅ Interactive Streamlit interface
* ✅ Gender selection
* ✅ Age input
* ✅ Estimated Salary input
* ✅ Feature scaling using `StandardScaler`
* ✅ Pre-trained KNN model
* ✅ Real-time purchase prediction
* ✅ User-friendly interface
* ✅ 92.5% test accuracy

---

## 🤖 Machine Learning Model

### K-Nearest Neighbors (KNN)

KNN is a supervised Machine Learning classification algorithm that predicts the class of a new data point based on its nearest neighboring data points.

Since KNN is a distance-based algorithm, feature scaling is important when the input features have different numerical ranges.

### Model Configuration

| Parameter           | Value                         |
| ------------------- | ----------------------------- |
| Algorithm           | K-Nearest Neighbors           |
| Number of Neighbors | 5                             |
| Preprocessing       | StandardScaler                |
| Problem Type        | Binary Classification         |
| Input Features      | Gender, Age, Estimated Salary |
| Test Accuracy       | **92.5%**                     |
| Output              | Purchased / Not Purchased     |

---

## 📊 Dataset

The project uses the **Social Network Ads** dataset.

### Dataset Features

| Feature           | Description                |
| ----------------- | -------------------------- |
| `User ID`         | Unique customer identifier |
| `Gender`          | Customer gender            |
| `Age`             | Customer age               |
| `EstimatedSalary` | Estimated customer salary  |
| `Purchased`       | Purchase decision          |

The `Purchased` column is the target variable.

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
KNN Model Training
   ↓
Model Evaluation
   ↓
Save Model & Scaler
   ↓
Streamlit Application
   ↓
Customer Input
   ↓
Purchase Prediction
```

---

## 📈 Model Performance

The KNN model was evaluated with and without feature scaling.

| Model               |  Accuracy |
| ------------------- | --------: |
| KNN Without Scaling |     82.5% |
| KNN With Scaling    | **92.5%** |

### 🏆 Result

Feature scaling improved the KNN model's accuracy from **82.5% to 92.5%**.

This demonstrates the importance of feature scaling for distance-based algorithms such as KNN.

---

## 📸 Project Screenshot

The Streamlit application screenshot is available in the `screenshots` folder of this repository.

### Streamlit Application

Click the screenshot below to open the **full-size image**.

[![Social Network Ads Purchase Prediction](https://github.com/shivani14012004/social-network-ads-purchase-prediction/blob/main/screenshots/app-interface.png.png
?raw=true)](https://github.com/shivani14012004/social-network-ads-purchase-prediction/blob/main/screenshots/app-interface.png.png
)

---

## 📂 Repository Structure

```text
social-network-ads-purchase-prediction/
│
├── screenshots/
│   └── app-interface.png
│
├── app.py
├── Social_Net_class.csv
├── knn_with_scaling.pkl
├── knn_without_scaling.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

| File / Folder             | Description                    |
| ------------------------- | ------------------------------ |
| `app.py`                  | Streamlit application          |
| `Social_Net_class.csv`    | Social Network Ads dataset     |
| `knn_with_scaling.pkl`    | Trained KNN model with scaling |
| `knn_without_scaling.pkl` | KNN model without scaling      |
| `scaler.pkl`              | Saved StandardScaler           |
| `requirements.txt`        | Required Python libraries      |
| `screenshots/`            | Project screenshots            |
| `README.md`               | Project documentation          |
| `.gitignore`              | Git ignored files              |

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**
* **Pickle**
* **Git**
* **GitHub**

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shivani14012004/social-network-ads-purchase-prediction.git
```

### 2. Navigate to the Project Folder

```bash
cd social-network-ads-purchase-prediction
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 🖥️ How to Use the Application

1. Open the Streamlit application.
2. Select the customer's Gender.
3. Enter the customer's Age.
4. Enter the Estimated Salary.
5. Click the **Predict** button.
6. The application displays whether the customer is likely to purchase the product.

---

## 🔮 Example Prediction

### Input

```text
Gender = Female
Age = 35
Estimated Salary = 70000
```

### Output

```text
Purchased
```

The actual prediction depends on the trained KNN model.

---

## 🎓 Key Learning Outcomes

Through this project, I learned:

* Data preprocessing using Pandas
* Feature selection
* Feature scaling using `StandardScaler`
* K-Nearest Neighbors classification
* Comparing models with and without scaling
* Model evaluation
* Saving Machine Learning models using Pickle
* Building interactive applications using Streamlit
* Managing Machine Learning projects using GitHub

---

## 🚀 Future Improvements

Possible improvements include:

* Add more customer-related features.
* Improve the Streamlit user interface.
* Display prediction probabilities.
* Add interactive data visualizations.
* Compare KNN with Logistic Regression.
* Compare KNN with Decision Tree and Random Forest.
* Add model performance charts.
* Improve model hyperparameter tuning.
* Deploy the application online.

---

## 👩‍💻 Author

**Shivani Patil**

Machine Learning | Python | Data Science | AI

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.


