import os
import joblib
import pandas as pd

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load trained model
MODEL_PATH = os.path.join(BASE_DIR, "models", "fake_profile_model.pkl")

model = joblib.load(MODEL_PATH)


def predict_fake_profile(
    username,
    display_name,
    bio,
    followers,
    following,
    posts,
    private,
    external_url,
    profile_pic
):

    # Feature engineering
    nums_length_username = sum(c.isdigit() for c in username) / max(len(username), 1)

    fullname_words = len(display_name.split())

    nums_length_fullname = sum(c.isdigit() for c in display_name) / max(len(display_name), 1)

    name_equals_username = int(
        username.lower().replace("_", "") ==
        display_name.lower().replace(" ", "")
    )

    description_length = len(bio)

    features = pd.DataFrame([{
        "profile pic": profile_pic,
        "nums/length username": nums_length_username,
        "fullname words": fullname_words,
        "nums/length fullname": nums_length_fullname,
        "name==username": name_equals_username,
        "description length": description_length,
        "external URL": external_url,
        "private": private,
        "#posts": posts,
        "#followers": followers,
        "#follows": following
    }])

    prediction = model.predict(features)[0]

    confidence = round(max(model.predict_proba(features)[0]) * 100, 2)

    if prediction == 1:
        result = "Fake Profile"
    else:
        result = "Genuine Profile"

    return {
        "prediction": result,
        "confidence": confidence
    }