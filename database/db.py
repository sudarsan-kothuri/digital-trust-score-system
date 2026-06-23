import sqlite3


def save_profile(username, display_name, trust_score, category):

    conn = sqlite3.connect("database/social_trust.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO profiles
        (username, display_name, trust_score, category)
        VALUES (?, ?, ?, ?)
        """,
        (username, display_name, trust_score, category)
    )

    conn.commit()
    conn.close()


def get_profiles():

    conn = sqlite3.connect("database/social_trust.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT username,
               display_name,
               trust_score,
               category
        FROM profiles
        ORDER BY id DESC
        """
    )

    profiles = cursor.fetchall()

    conn.close()

    return profiles