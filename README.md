# 🛍️ Social Network Ads Purchase Prediction

### K-Nearest Neighbors (KNN) | Machine Learning | Streamlit

A professional **Machine Learning web application** that predicts whether a customer is likely to purchase a product after viewing a social network advertisement.

The project uses the **K-Nearest Neighbors (KNN)** algorithm with **feature scaling** and provides an interactive prediction interface built with **Streamlit**.

---

## 📌 Project Overview

The goal of this project is to predict customer purchase behavior based on demographic and salary information.

The model uses the following customer features:

* **Gender**
* **Age**
* **Estimated Salary**

A **StandardScaler** is used to scale the numerical features before making predictions.

The trained KNN model classifies the customer into one of two categories:

* **0 → Not Purchased**
* **1 → Purchased**

The trained model and scaler are saved as `.pkl` files and loaded by the Streamlit application.

---

## 🌐 Live Demo

🚀 **Try the application online:**

👉 [**Live Demo – Social Network Ads Purchase Prediction**](YOUR_DEPLOYED_STREAMLIT_URL)

> Replace `YOUR_DEPLOYED_STREAMLIT_URL` with your actual Streamlit deployment URL.

Example:

```text
https://your-app-name.streamlit.app
```

---

## 📸 Application Screenshot

### Streamlit Application Output

<p align="center">
  <img src="screenshots/app.png"
       alt="Social Network Ads Purchase Prediction Streamlit Output"
       width="800">
</p>

The screenshot above shows the Streamlit application interface and prediction output.

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

| Parameter               | Details                       |
| ----------------------- | ----------------------------- |
| **Algorithm**           | K-Nearest Neighbors (KNN)     |
| **Number of Neighbors** | 5                             |
| **Preprocessing**       | StandardScaler                |
| **Problem Type**        | Binary Classification         |
| **Input Features**      | Gender, Age, Estimated Salary |
| **Test Accuracy**       | **92.5%**                     |
| **Output**              | Purchased / Not Purchased     |

---

## 📊 Dataset

The project is based on the **Social Network Ads** dataset.

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

## 📂 Repository Structure

```text
social-network-ads-purchase-prediction/
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

### File Description

| File / Folder          | Description                             |
| ---------------------- | --------------------------------------- |
| `app.py`               | Streamlit application                   |
| `knn_with_scaling.pkl` | Trained KNN model                       |
| `scaler.pkl`           | Saved StandardScaler                    |
| `requirements.txt`     | Required Python libraries               |
| `screenshots/`         | Project screenshots                     |
| `screenshots/app.png`  | Streamlit application output screenshot |
| `README.md`            | Project documentation                   |

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
2. Select the customer's **Gender**.
3. Enter the customer's **Age**.
4. Enter the customer's **Estimated Salary**.
5. Click the **Predict** button.
6. The application displays whether the customer is likely to purchase the product.

---

## 📈 Model Performance

The KNN model was evaluated with and without feature scaling.

| Model                |  Accuracy |
| -------------------- | --------: |
| KNN without Scaling  | **82.5%** |
| **KNN with Scaling** | **92.5%** |

### 📌 Result

Feature scaling significantly improved the KNN model's performance from **82.5% to 92.5%**.

This demonstrates why feature scaling is important for distance-based algorithms such as KNN.

---

## 💡 Why KNN?

K-Nearest Neighbors is a classification algorithm that predicts the class of a new data point based on the classes of its nearest neighboring data points.

Since KNN calculates distances between data points, **feature scaling is important** when features have different numerical ranges.

In this project, `StandardScaler` is used before prediction.

---

## 🚀 Deployment

The Streamlit application can be deployed using platforms such as:

* **Streamlit Community Cloud**
* **Render**
* **Hugging Face Spaces**

### 🌐 Live Application

👉 [**Open Live Demo**](http://localhost:8501)

After deployment, replace `YOUR_DEPLOYED_STREAMLIT_URL` with your actual application URL.

---

## 📸 Screenshots

The project screenshots are stored inside the existing `screenshots/` folder.

```text
screenshots/
└── app-interface.png

```

The main application screenshot is displayed above in the **Application Screenshot** section.

---

## 📦 Requirements

The project requires the following Python libraries:

```text
streamlit
pandas
numpy
scikit-learn
```

---

## 🎓 Key Learning Outcomes

Through this project, I learned:

* Data preprocessing using Pandas.
* Feature scaling using `StandardScaler`.
* Implementing K-Nearest Neighbors.
* Comparing KNN performance with and without scaling.
* Evaluating classification models.
* Saving trained models using Pickle.
* Building an interactive Machine Learning application using Streamlit.
* Managing and documenting Machine Learning projects using GitHub.

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

---

⭐ **If you found this project useful, consider giving the repository a star!**
