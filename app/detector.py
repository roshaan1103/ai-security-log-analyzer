def analyze(features, model):
    predictions = model.predict(features[["failed_attempts", "unique_users"]])
    results = []

    for i, row in features.iterrows():
        reason = "Normal activity"
        severity = "low"

        if row["failed_attempts"] > 5:
            reason = "Brute-force attempt detected"
            severity = "high"
        elif row["unique_users"] > 3:
            reason = "Multiple user attempts from same IP"
            severity = "medium"

        status = "suspicious" if predictions[i] == -1 else "normal"

        results.append({
            "ip": row["ip"],
            "status": status,
            "reason": reason,
            "severity": severity
        })

    return results