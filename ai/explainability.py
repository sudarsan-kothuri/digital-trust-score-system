def generate_explanation(
    username,
    display_name,
    bio,
    followers,
    following,
    posts,
    private,
    external_url,
    ml_prediction
):

    reasons = []

    # Username analysis

    number_count = sum(
        c.isdigit()
        for c in username
    )

    if number_count > 2:
        reasons.append(
            "Username contains many numbers"
        )


    # Follower analysis

    if followers < 50:
        reasons.append(
            "Very low follower count"
        )


    # Following ratio

    if followers > 0:

        ratio = following / followers

        if ratio > 5:
            reasons.append(
                "Suspicious following-to-follower ratio"
            )


    # Bio analysis

    if len(bio) < 15:

        reasons.append(
            "Very short biography"
        )


    # Posts

    if posts < 5:

        reasons.append(
            "Very low post activity"
        )


    # External URL

    if external_url == 0:

        reasons.append(
            "No external verification link"
        )


    # Private account

    if private == 1:

        reasons.append(
            "Private account limits verification"
        )


    # If nothing found

    if len(reasons) == 0:

        reasons.append(
            "No major suspicious patterns detected"
        )


    return {

        "prediction": ml_prediction,

        "reasons": reasons

    }