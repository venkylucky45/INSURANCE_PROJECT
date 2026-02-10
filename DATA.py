import pandas as pd
import numpy as np
import random

def generate_travel_frequency():
    choice = random.choice(["daily", "weekly", "monthly", "seasonal", "random"])
    mapping = {
        "daily": random.randint(25, 30),
        "weekly": random.randint(8, 12),
        "monthly": random.randint(1, 3),
        "seasonal": random.randint(1, 2),
        "random": random.randint(0, 1)
    }
    return mapping[choice]

def generate_dataset(n=1000):
    df = pd.DataFrame({
        "customer_id": [f"CUST_{i+1}" for i in range(n)],
        "age": np.random.randint(18, 70, n),
        "gender": np.random.choice(["Male", "Female"], n),
        "city": np.random.choice(["Mumbai", "Delhi", "Hyderabad", "Pune", "Chennai"], n),
        "travel_frequency": [generate_travel_frequency() for _ in range(n)],
        "travel_type": np.random.choice(["Business", "Personal", "Seasonal"], n),
        "past_claims": np.random.randint(0, 3, n),
        "loyalty_score": np.random.randint(10, 100, n),
        "risk_score": np.random.randint(5, 90, n),
        "segment": [-1] * n
    })

    df.to_csv("data/raw/travel_insurance_customers.csv", index=False)
    print("Dataset generated at: data/raw/travel_insurance_customers.csv")

generate_dataset()
