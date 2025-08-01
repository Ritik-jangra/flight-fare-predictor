# ✈️ Flight Fare Predictor

Estimate the price of flight tickets based on various inputs like airline, route, schedule, stops, and travel class using a machine learning model trained on real-world data.

---

## 🚀 Live Demo

[Click here to use the app]([https://your-streamlit-cloud-link.com](https://flight-fare-predictor-nikhur5ujscpvstcrdazmz.streamlit.app/)) <!-- Add your actual Streamlit Cloud URL here -->

---

## 📂 GitHub Repository

[GitHub Repo](https://github.com/Ritik-jangra/flight-fare-predictor) <!-- Add your repo URL here -->

---

## 📌 Features

- Predicts flight ticket price based on user inputs
- Clean and responsive **dark-themed Streamlit UI**
- Custom form with date & time pickers
- Input validation for departure and arrival times
- Displays fare instantly on submission
- Compares multiple regression models behind the scenes

---

## 📊 Tech Stack

- **Frontend:** Streamlit (custom CSS styling)
- **Backend:** Python, Pandas, NumPy
- **Machine Learning:** scikit-learn (Random Forest)
- **Model Export:** joblib
- **Dataset Handling:** pandas, one-hot encoding

---

## 🧠 Model Information

Three models were trained and evaluated:

| Model              | R² Score | MAE     | RMSE    |
|-------------------|----------|---------|---------|
| Linear Regression | 0.4431   | 4543.11 | 6221.53 |
| Decision Tree     | 0.8493   | 2141.85 | 3186.23 |
| **Random Forest** | **0.9034** | **1812.24** | **2564.77** |

> ✅ Final Model: **Random Forest Regressor** (Best performance)

---

## 📁 Project Structure

Flight-Fare-Predictor/
│
├── app.py # Streamlit app interface
├── Data_Cleaning.ipynb # Preprocessing notebook
├── Model_Train.ipynb # Model training + evaluation
├── Fully Cleaned data.csv # Cleaned dataset
├── random_forest_model.pkl # Trained model (Random Forest)
├── model_features.pkl # Feature list used by model
└── requirements.txt # Dependencies


---

## 🧼 Dataset Details

- **Source:** Kaggle / Open Flight Dataset
- **Rows:** ~300,000
- **Features:**
  - Airline, Source City, Destination City
  - Class, Stops
  - Departure/Arrival Times
  - Flight Duration
  - Ticket Price (Target)

---

## ⚙️ How It Works

1. User enters flight details in the app
2. Input is converted to model-ready format
3. Model predicts fare based on trained Random Forest regressor
4. Predicted fare is shown with a clean UI message

---

## 🔧 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Ritik-jangra/flight-fare-predictor.git
cd flight-fare-predictor

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

📦 Requirements.txt
pandas
numpy
scikit-learn
streamlit
joblib
tabulate

👨‍💻 Author
Ritik Jangra
MCA Student 
