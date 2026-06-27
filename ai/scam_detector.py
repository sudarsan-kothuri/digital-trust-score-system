import re

SCAM_PATTERNS = {
    "Investment Scam": [
        "crypto",
        "bitcoin",
        "investment",
        "double money",
        "profit",
        "forex",
        "trading",
        "guaranteed return"
    ],

    "Job Scam": [
        "work from home",
        "earn daily",
        "part time",
        "job offer",
        "salary",
        "easy income"
    ],

    "Loan Scam": [
        "loan",
        "instant loan",
        "credit",
        "emi",
        "low interest"
    ],

    "Lottery Scam": [
        "winner",
        "lottery",
        "claim prize",
        "gift card",
        "congratulation"
    ],

    "Romance Scam": [
        "love",
        "relationship",
        "widow",
        "military officer",
        "soulmate"
    ]
}


def analyze_bio(bio):

    keywords = []

    scam_words = [
        "free",
        "giveaway",
        "crypto",
        "investment",
        "win",
        "money"
    ]


    for word in scam_words:

        if word.lower() in bio.lower():

            keywords.append(word)



    risk = len(keywords) * 20


    if risk >= 60:
        category = "High Scam Risk"

    elif risk >= 20:
        category = "Medium Scam Risk"

    else:
        category = "Low Scam Risk"



    confidence = min(
        95,
        50 + risk
    )



    return {

        "category": category,

        "confidence": confidence,

        "keywords": keywords,

        "risk": risk

    }