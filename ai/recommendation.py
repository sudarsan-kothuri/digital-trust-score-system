def generate_recommendation(trust_score,
                            impersonation_risk,
                            scam_category):

    if trust_score < 30:
        return {
            "action": "Immediate Investigation",
            "priority": "Critical",
            "color": "danger",
            "reason": "Very low trust score."
        }

    elif impersonation_risk == "High":
        return {
            "action": "Manual Identity Verification",
            "priority": "High",
            "color": "warning",
            "reason": "Possible impersonation detected."
        }

    elif scam_category != "Safe":
        return {
            "action": "Monitor Account Activity",
            "priority": "Medium",
            "color": "warning",
            "reason": f"Possible {scam_category} detected."
        }

    else:
        return {
            "action": "No Immediate Action",
            "priority": "Low",
            "color": "success",
            "reason": "Profile appears legitimate."
        }