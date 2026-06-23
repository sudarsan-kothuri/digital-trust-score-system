from difflib import SequenceMatcher

def check_impersonation(username, display_name):

    similarity = SequenceMatcher(
        None,
        username.lower(),
        display_name.lower()
    ).ratio()

    similarity_percent = round(similarity * 100)

    if similarity_percent >= 90:
        risk = "High"
    elif similarity_percent >= 70:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "similarity": similarity_percent,
        "risk": risk
    }