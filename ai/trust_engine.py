def calculate_trust_score(profile_risk, impersonation_risk):

    score = 100

    # Deduct profile risk
    score -= profile_risk

    # Deduct impersonation risk
    if impersonation_risk == "High":
        score -= 30
    elif impersonation_risk == "Medium":
        score -= 15
    elif impersonation_risk == "Low":
        score -= 5

    # Keep score between 0 and 100
    score = max(0, min(100, score))

    # Category
    if score >= 80:
        category = "Trusted"
    elif score >= 50:
        category = "Medium Risk"
    else:
        category = "High Risk"

    return {
        "trust_score": score,
        "category": category
    }