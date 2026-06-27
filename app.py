from flask import Flask, render_template, request, send_from_directory
import os

# AI Modules
from ai.profile_analyzer import analyze_profile
from ai.image_detector import analyze_image
from ai.impersonation_detector import check_impersonation
from ai.trust_engine import calculate_trust_score

from ai.ml_detector import predict_fake_profile
from ai.explainability import generate_explanation

from ai.scam_detector import analyze_bio
from ai.recommendation import generate_recommendation


# Database
from database.db import save_profile, get_profiles


# PDF
from reports.report_generator import generate_report



app = Flask(__name__)


UPLOAD_FOLDER = "uploads"


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)



# ----------------------------
# HOME
# ----------------------------

@app.route("/")
def home():

    return render_template(
        "index.html"
    )



# ----------------------------
# IMAGE ACCESS
# ----------------------------

@app.route("/uploads/<filename>")
def uploaded_file(filename):

    return send_from_directory(
        "uploads",
        filename
    )



# ----------------------------
# PDF DOWNLOAD
# ----------------------------

@app.route("/download/<filename>")
def download(filename):

    return send_from_directory(
        "reports/generated",
        filename,
        as_attachment=True
    )




# ----------------------------
# RESULT
# ----------------------------

@app.route("/result", methods=["POST"])
def result():


    username = request.form["username"]

    display_name = request.form["display_name"]

    bio = request.form["bio"]



    followers = int(
        request.form["followers"]
    )


    following = int(
        request.form["following"]
    )


    account_age = int(
        request.form["account_age"]
    )


    posts = int(
        request.form["posts"]
    )


    private = int(
        request.form["private"]
    )


    external_url = int(
        request.form["external_url"]
    )


    profile_pic = int(
        request.form["profile_pic"]
    )



    # IMAGE


    image = request.files["profile_image"]


    image_path = os.path.join(
        UPLOAD_FOLDER,
        image.filename
    )


    image.save(image_path)



    # ----------------------------
    # PROFILE ANALYSIS
    # ----------------------------


    analysis = analyze_profile(

        followers,
        following,
        account_age

    )



    # ----------------------------
    # IMAGE ANALYSIS
    # ----------------------------


    image_analysis = analyze_image(

        image_path

    )



    # ----------------------------
    # IMPERSONATION
    # ----------------------------


    impersonation = check_impersonation(

        username,

        display_name

    )



    # ----------------------------
    # SCAM ANALYSIS
    # ----------------------------


    scam_analysis = analyze_bio(

        bio

    )
    print(scam_analysis)



    # ----------------------------
    # ML PREDICTION
    # ----------------------------


    ml_prediction = predict_fake_profile(

        username,

        display_name,

        bio,

        followers,

        following,

        posts,

        private,

        external_url,

        profile_pic

    )
    # ----------------------------
    # EXPLAINABLE AI
    # ----------------------------


    explanation = generate_explanation(

        username,

        display_name,

        bio,

        followers,

        following,

        posts,

        private,

        external_url,

        ml_prediction["prediction"]

    )



    # ----------------------------
    # TOTAL RISK
    # ----------------------------


    total_profile_risk = (

        analysis["risk_score"]

        +

        image_analysis["image_risk"]

        +

        scam_analysis["risk"]

    )



    # ----------------------------
    # TRUST SCORE
    # ----------------------------


    trust = calculate_trust_score(

        total_profile_risk,

        impersonation["risk"]

    )



    # ----------------------------
    # POLICE RECOMMENDATION
    # ----------------------------


    recommendation = generate_recommendation(

        trust["trust_score"],

        impersonation["risk"],

        scam_analysis["category"]

    )



    # ----------------------------
    # PDF REPORT
    # ----------------------------


    report_file = generate_report({

    "username": username,

    "display_name": display_name,

    "trust_score": trust["trust_score"],

    "category": trust["category"],


    "ml_prediction":
    ml_prediction["prediction"],


    "ml_confidence":
    ml_prediction["confidence"],


    "explanation":
    explanation["reasons"],


    "image_reason":
    image_analysis["reason"],


    "image_risk":
    image_analysis["image_risk"],


    "similarity":
    impersonation["similarity"],


    "impersonation_risk":
    impersonation["risk"],


    "scam_category":
    scam_analysis["category"],


    "scam_confidence":
    scam_analysis["confidence"],


    "recommendation":
    recommendation["action"],

    "recommendation_reason":
    recommendation["reason"],


    "priority":
    recommendation["priority"]

})



    # ----------------------------
    # SAVE DATABASE
    # ----------------------------


    save_profile(

        username,

        display_name,

        trust["trust_score"],

        trust["category"]

    )



    # ----------------------------
    # RESULT PAGE
    # ----------------------------


    return render_template(

        "result.html",


        username=username,

        display_name=display_name,


        image_file=image.filename,


        risk_score=

        analysis["risk_score"],


        reasons=

        analysis["reasons"],



        image_risk=

        image_analysis["image_risk"],


        image_reason=

        image_analysis["reason"],



        similarity=

        impersonation["similarity"],


        impersonation_risk=

        impersonation["risk"],



        trust_score=

        trust["trust_score"],


        category=

        trust["category"],



        ml_prediction=

        ml_prediction["prediction"],



        ml_confidence=

        ml_prediction["confidence"],



        explanation=

        explanation["reasons"],



        scam_category=

        scam_analysis["category"],


        scam_confidence=

        scam_analysis["confidence"],


        scam_keywords=

        scam_analysis["keywords"],



        recommendation=

        recommendation["action"],


        priority=

        recommendation["priority"],


        recommendation_reason=

        recommendation["reason"],



        report_file=

        report_file

    )





# ----------------------------
# DASHBOARD
# ----------------------------


@app.route("/dashboard")
def dashboard():

    profiles = get_profiles()

    total_cases = len(profiles)

    trusted = 0
    medium = 0
    high = 0
    total_score = 0

    # Replace your old loop with this one
    for profile in profiles:

        score = int(profile[2])      # Trust Score
        category = profile[3]        # Category

        total_score += score

        if category == "Trusted":
            trusted += 1

        elif category == "Medium Risk":
            medium += 1

        elif category == "High Risk":
            high += 1

    average_score = round(total_score / total_cases) if total_cases else 0

    return render_template(
        "dashboard.html",
        profiles=profiles,
        total_cases=total_cases,
        trusted=trusted,
        medium=medium,
        high=high,
        average_score=average_score
    )





# ----------------------------
# RUN
# ----------------------------


if __name__ == "__main__":

    app.run(debug=True)