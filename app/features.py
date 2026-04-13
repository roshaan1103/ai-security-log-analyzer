import pandas as pd

def extract_features(parsed_logs):
    df = pd.DataFrame(parsed_logs)

    features = df.groupby("ip").agg({
        "status": "count",
        "user": "nunique"
    }).rename(columns={
        "status": "failed_attempts",
        "user": "unique_users"
    })

    return features.reset_index()