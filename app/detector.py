from app.mitre import MITRE_MAPPING

def analyze(features, model):
    predictions = model.predict(features[["failed_attempts", "unique_users"]])
    results = []

    for i, row in features.iterrows():

        if row["failed_attempts"] > 5:
            status = "suspicious"
            reason = "Brute-force attempt detected"
            severity = "high"
            mitre = MITRE_MAPPING["brute_force"]

        elif row["unique_users"] > 3:
            status = "suspicious"
            reason = "Multiple user attempts from same IP"
            severity = "medium"
            mitre = MITRE_MAPPING["credential_stuffing"]

        elif predictions[i] == -1:
            status = "suspicious"
            reason = "Anomalous behavior detected by ML model"
            severity = "medium"
            mitre = MITRE_MAPPING["anomalous_behavior"]

        else:
            status = "normal"
            reason = "Normal activity"
            severity = "low"
            mitre = None

        result = {
            "ip": row["ip"],
            "status": status,
            "reason": reason,
            "severity": severity
        }

        if mitre:
            result["mitre_technique_id"] = mitre["technique_id"]
            result["mitre_technique_name"] = mitre["technique_name"]

        results.append(result)

    return results