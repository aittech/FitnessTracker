import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os

def train_calorie_models(csv_path="data/workouts.csv"):
    """Train a separate linear regression model for each activity type."""
    if not os.path.exists(csv_path):
        return {}

    data = pd.read_csv(csv_path)
    if len(data) < 5:
        return {}

    models = {}
    for activity in data["Activity"].unique():
        subset = data[data["Activity"] == activity]
        if len(subset) >= 3:  # train only if at least 3 samples for that activity
            X = subset[["Duration", "Weight"]]
            y = subset["CaloriesBurned"]
            model = LinearRegression()
            model.fit(X, y)
            models[activity] = model
    return models


def predict_calories(models, duration, weight, activity):
    """Predict calories burned for a given activity using its specific model."""
    if activity in models:
        X_new = [[duration, weight]]
        return float(models[activity].predict(X_new)[0])
    else:
        # fallback in case not enough data for this activity
        return 6.0 * weight * (duration / 60)


def get_model_accuracy(csv_path="data/workouts.csv"):
    """Calculate average R² accuracy across all activity models."""
    if not os.path.exists(csv_path):
        return None

    data = pd.read_csv(csv_path)
    if len(data) < 5:
        return None

    scores = []
    for activity in data["Activity"].unique():
        subset = data[data["Activity"] == activity]
        if len(subset) >= 3:
            X = subset[["Duration", "Weight"]]
            y = subset["CaloriesBurned"]
            model = LinearRegression()
            model.fit(X, y)
            predictions = model.predict(X)
            scores.append(r2_score(y, predictions))

    if not scores:
        return None
    avg_accuracy = sum(scores) / len(scores) * 100
    return round(avg_accuracy, 2)
