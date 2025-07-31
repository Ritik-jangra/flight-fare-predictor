# import necessary libraries

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error
from tabulate import tabulate
import joblib

# Load the dataset
df = pd.read_csv("Fully Cleaned data.csv")

# Features and target seperation
X = df.drop("price", axis=1)
y = df["price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=10, random_state=42)
}

# Evaluate models and store results
results = []

# Model Evaluation
print("Model Performance:\n")

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    results.append([name, f"{r2:.4f}", f"{mae:.2f}", f"{rmse:.2f}"])
    
    print(f"{name}")
    print(f"R² Score : {r2:.4f}")
    print(f"MAE      : {mae:.2f}")
    print(f"RMSE     : {rmse:.2f}\n")

# Summary Table
print(tabulate(results, headers=["Model", "R² Score", "MAE", "RMSE"], tablefmt="fancy_grid"))

# Save the best model (Random Forest)
best_model = models["Random Forest"]
joblib.dump(best_model, "random_forest_model.pkl")
print("Random Forest model saved successfully as 'random_forest_model.pkl'")
joblib.dump(X.columns.tolist(), "model_features.pkl")