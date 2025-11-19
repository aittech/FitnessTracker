# utils.py  – shared helper functions for FitnessTrackerApp

def calculate_formula_calories(activity, duration, weight):
    """
    Estimate calories burned using MET values.
    activity: name of the exercise
    duration: duration in minutes
    weight: user weight in kilograms
    """
    MET = {
        "Running": 9.8,
        "Cycling": 7.5,
        "Walking": 3.8,
        "Strength": 6.0
    }

    hours = duration / 60
    return MET.get(activity, 5.0) * weight * hours
