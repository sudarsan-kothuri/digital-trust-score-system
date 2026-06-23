def analyze_profile(followers, following, account_age):

    risk_score = 0
    reasons = []

    followers = int(followers)
    following = int(following)
    account_age = int(account_age)

    if account_age < 30:
        risk_score += 30
        reasons.append("Very new account")

    if followers < 50:
        risk_score += 20
        reasons.append("Very low followers")

    if following > followers * 5:
        risk_score += 25
        reasons.append("Suspicious following ratio")

    return {
        "risk_score": risk_score,
        "reasons": reasons
    }