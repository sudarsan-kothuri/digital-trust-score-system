import cv2

def analyze_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        return {
            "image_risk": 50,
            "reason": "Invalid image"
        }

    height, width = image.shape[:2]

    if width < 200 or height < 200:
        risk = 30
        reason = "Low resolution image"
    else:
        risk = 10
        reason = "Good image quality"

    return {
        "image_risk": risk,
        "reason": reason
    }