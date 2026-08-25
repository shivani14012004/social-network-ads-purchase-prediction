# 🛍️ Social Network Ads Purchase Prediction

### K-Nearest Neighbors (KNN) | Machine Learning | Streamlit

A Machine Learning web application that predicts whether a customer is likely to purchase a product after viewing a social network advertisement.

The project uses the **K-Nearest Neighbors (KNN)** classification algorithm with **feature scaling** and provides an interactive prediction interface using **Streamlit**.

---

## 🌐 Live Demo

🚀 **Try the application online:**

👉 **[Live Demo – Social Network Ads Purchase Prediction](http://localhost:8501)**

> ⚠️ Replace `YOUR_LIVE_STREAMLIT_URL` with your actual deployed Streamlit application URL.

Example:

```text
https://your-app-name.streamlit.app
```

---

## 📸 Application Screenshot

### Streamlit Application

![Streamlit Application Screenshot](screenshots/app-interface.png)

The screenshot above shows the interactive Streamlit application and its prediction interface.

---

## 📌 Project Overview

The goal of this project is to predict whether a customer will purchase a product after viewing a social network advertisement.

The model uses customer information such as:

* Gender
* Age
* Estimated Salary

The target variable is:

* `0` → Not Purchased
* `1` → Purchased

Feature scaling is performed using **StandardScaler** before applying the KNN algorithm.

---

## 🎯 Project Objectives

* Analyze customer purchase behavior
* Perform data preprocessing
* Apply feature scaling
* Build a K-Nearest Neighbors classification model
* Compare KNN performance with and without scaling
* Save the trained machine learning model
* Build an interactive Streamlit application
* Make real-time purchase predictions
* Deploy the application online

---

## 🚀 Key Features

* ✅ Interactive Streamlit interface
* ✅ Gender selection
* ✅ Age input
* ✅ Estimated Salary input
* ✅ Real-time prediction
* ✅ KNN classification
* ✅ StandardScaler preprocessing
* ✅ Pre-trained machine learning model
* ✅ User-friendly interface
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
| KNN without Scaling |     82.5% |
| KNN with Scaling    | **92.5%** |

### Result

Feature scaling improved the model accuracy from **82.5% to 92.5%**.

This demonstrates the importance of feature scaling for distance-based algorithms such as KNN.

---

## 💡 Why KNN?

K-Nearest Neighbors is a supervised machine learning algorithm used for classification.

KNN predicts the class of a new data point based on the classes of its nearest neighboring data points.

Since KNN calculates distances between data points, feature scaling is important when the features have different numerical ranges.

In this project, `StandardScaler` is used before making predictions.

---

## 📂 Repository Structure

```text
social-network-ads-purchase-prediction/
│
├── screenshots/
│   └── app.png
│
├── app.py
├── Social_Net_class.csv
├── knn_with_scaling.pkl
├── knn_without_scaling.pkl
├── scaler.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

| File / Folder             | Description                    |
| ------------------------- | ------------------------------ |
| `app.py`                  | Streamlit application          |
| `Social_Net_class.csv`    | Dataset                        |
| `knn_with_scaling.pkl`    | Trained KNN model with scaling |
| `knn_without_scaling.pkl` | KNN model without scaling      |
| `scaler.pkl`              | Saved StandardScaler           |
| `requirements.txt`        | Required Python libraries      |
| `screenshots/`            | Application screenshots        |
| `README.md`               | Project documentation          |
| `.gitignore`              | Files excluded from GitHub     |

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle
* Git
* GitHub

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

The application will open locally at:

```text
http://localhost:8501
```

---

## 🖥️ How to Use the Application

1. Open the Streamlit application.
2. Select the customer's gender.
3. Enter the customer's age.
4. Enter the estimated salary.
5. Click the **Predict** button.
6. The application displays the predicted purchase result.

---

## 📸 Project Screenshots

### Application Interface

![Streamlit Application](app-interface.png)

> You can add more screenshots to the `screenshots` folder and display them here using the same format.

Example:

```markdown
![Prediction Result](screenshots/prediction.png)
```

---

## 🚀 Deployment

This application can be deployed using:

* Streamlit Community Cloud
* Render
* Hugging Face Spaces

### 🌐 Deployed Application

**Live Demo:** [Open the deployed application]( http://localhost:8501)

---

## 🔮 Future Improvements

* Add more machine learning algorithms
* Improve model performance through hyperparameter tuning
* Add confusion matrix visualization
* Add prediction probability
* Improve the Streamlit UI
* Add interactive data visualizations
* Deploy with a custom domain

---

## 👩‍💻 Author

**Shivani Patil**

GitHub: [@shivani14012004](https://github.com/shivani14012004)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**Thank you for visiting this project!**
