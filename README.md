# 🛍️ Social Network Ads Purchase Prediction

### K-Nearest Neighbors (KNN) | Machine Learning | Streamlit

A professional **Machine Learning web application** that predicts whether a customer is likely to purchase a product after viewing a social network advertisement. The project uses the **K-Nearest Neighbors (KNN)** algorithm with **feature scaling** and provides an interactive prediction interface built with **Streamlit**.

---

## 📌 Project Overview

The goal of this project is to predict customer purchase behavior based on demographic and salary information.

The model uses the following customer features:

* **Gender**
* **Age**
* **Estimated Salary**

A **StandardScaler** is used to scale the numerical features before making predictions. The trained KNN model then classifies the customer into one of two categories:

* **0 → Not Purchased**
* **1 → Purchased**

The trained model and scaler are saved as `.pkl` files and loaded by the Streamlit application.

---

## 🎯 Project Objectives

* Analyze customer purchase behavior.
* Apply data preprocessing and feature scaling.
* Build a K-Nearest Neighbors classification model.
* Evaluate model performance.
* Save the trained model using Pickle.
* Create an interactive Streamlit web application.
* Allow users to make real-time purchase predictions.

---

## 🚀 Key Features

* ✅ Interactive Streamlit user interface
* ✅ Gender selection
* ✅ Age and salary input
* ✅ Real-time purchase prediction
* ✅ Feature scaling using `StandardScaler`
* ✅ Pre-trained KNN model
* ✅ Simple and user-friendly interface
* ✅ Approximately **92.5% test accuracy**

---

## 🤖 Machine Learning Model

| Parameter           | Details                       |
| ------------------- | ----------------------------- |
| Algorithm           | K-Nearest Neighbors (KNN)     |
| Number of Neighbors | 5                             |
| Preprocessing       | StandardScaler                |
| Problem Type        | Binary Classification         |
| Input Features      | Gender, Age, Estimated Salary |
| Test Accuracy       | **92.5%**                     |
| Output              | Purchased / Not Purchased     |

---

## 📊 Dataset

The project is based on the **Social Network Ads** dataset.

### Dataset Features

| Feature         | Description                |
| --------------- | -------------------------- |
| User ID         | Unique customer identifier |
| Gender          | Customer gender            |
| Age             | Customer age               |
| EstimatedSalary | Estimated customer salary  |
| Purchased       | Purchase decision          |

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

## 📂 Repository Structure

```text
social-network-ads-knn/
│
├── app.py
├── knn_with_scaling.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

### File Description

| File                   | Description               |
| ---------------------- | ------------------------- |
| `app.py`               | Streamlit application     |
| `knn_with_scaling.pkl` | Trained KNN model         |
| `scaler.pkl`           | Saved StandardScaler      |
| `requirements.txt`     | Required Python libraries |
| `README.md`            | Project documentation     |

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**
* **Pickle**
* **Git & GitHub**

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/social-network-ads-knn.git
```

### 2. Navigate to the Project Folder

```bash
cd social-network-ads-knn
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
2. Select the customer's **Gender**.
3. Enter the customer's **Age**.
4. Enter the **Estimated Salary**.
5. Click the **Predict** button.
6. The application displays whether the customer is likely to purchase the product.

---

## 📈 Model Performance

The KNN model was evaluated with and without feature scaling.

| Model               |  Accuracy |
| ------------------- | --------: |
| KNN without Scaling | **82.5%** |
| KNN with Scaling    | **92.5%** |

### 📌 Result

Feature scaling significantly improved the KNN model's performance from **82.5% to 92.5%**.

This demonstrates why feature scaling is important for distance-based algorithms such as KNN.

---

## 💡 Why KNN?

K-Nearest Neighbors is a classification algorithm that predicts the class of a new data point based on the classes of its nearest neighboring data points.

Since KNN calculates distances between data points, **feature scaling is important** when features have different numerical ranges.

In this project, `StandardScaler` is used before prediction.

---

## 🌐 Deployment

This Streamlit application can be deployed using platforms such as:

* Streamlit Community Cloud
* Render
* Hugging Face Spaces

After deployment, add your live application URL to this README.

```text
Live Demo: YOUR_DEPLOYED_APP_URL
```

---

## 📸 Application Preview

Add screenshots of your Streamlit application here:

```markdown
![Application Screenshot](screenshots/app.png)
```

Recommended repository structure:

```text
social-network-ads-knn/
│
├── screenshots/
│   └── app.png
│
├── app.py
├── knn_with_scaling.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

## 📦 Requirements

Example `requirements.txt`:

```text
streamlit
pandas
numpy
scikit-learn
```

---

## 🔮 Future Improvements

* Add more customer-related features.
* Improve the Streamlit user interface.
* Display prediction probabilities.
* Add interactive data visualizations.
* Compare KNN with Logistic Regression, Decision Tree, and Random Forest.
* Deploy the application publicly.
* Add model performance charts.

---

## 👩‍💻 Author

**Shivani**

Machine Learning | Python | Data Science | AI

