from flask import Flask, render_template, request, send_from_directory
from ai.profile_analyzer import analyze_profile
from ai.impersonation_detector import check_impersonation
from ai.trust_engine import calculate_trust_score
from ai.image_detector import analyze_image

from database.db import save_profile, get_profiles

import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory("uploads", filename)


@app.route("/result", methods=["POST"])
def result():

    username = request.form["username"]
    display_name = request.form["display_name"]
    bio = request.form["bio"]
    followers = request.form["followers"]
    following = request.form["following"]
    account_age = request.form["account_age"]

    image = request.files["profile_image"]

    image_path = os.path.join(
        UPLOAD_FOLDER,
        image.filename
    )

    image.save(image_path)

    # Profile Analysis
    analysis = analyze_profile(
        followers,
        following,
        account_age
    )

    # Impersonation Analysis
    impersonation = check_impersonation(
        username,
        display_name
    )

    # Image Analysis
    image_analysis = analyze_image(
        image_path
    )

    # Combined Risk
    total_profile_risk = (
        analysis["risk_score"] +
        image_analysis["image_risk"]
    )

    # Trust Score
    trust = calculate_trust_score(
        total_profile_risk,
        impersonation["risk"]
    )

    # Save to Database
    save_profile(
        username,
        display_name,
        trust["trust_score"],
        trust["category"]
    )

    return render_template(
        "result.html",

        username=username,
        display_name=display_name,

        image_file=image.filename,

        risk_score=analysis["risk_score"],
        reasons=analysis["reasons"],

        similarity=impersonation["similarity"],
        impersonation_risk=impersonation["risk"],

        image_risk=image_analysis["image_risk"],
        image_reason=image_analysis["reason"],

        trust_score=trust["trust_score"],
        category=trust["category"]
    )


@app.route("/dashboard")
def dashboard():

    profiles = get_profiles()

    return render_template(
        "dashboard.html",
        profiles=profiles
    )


if __name__ == "__main__":
    app.run(debug=True)