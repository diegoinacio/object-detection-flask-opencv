from flask import Flask, render_template, request, Response, redirect, url_for
from flask_bootstrap import Bootstrap

from object_detection import *
from camera_settings import *


application = Flask(__name__)
Bootstrap(application)


check_settings()
VIDEO = VideoStreaming()


@application.route("/")
def home():
    TITLE = "Object detection"
    return render_template("index.html", TITLE=TITLE)


@application.route("/video_feed")
def video_feed():
    """
    Video streaming route.
    """
    return Response(
        VIDEO.show(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


# * Button requests
@application.route("/request_preview_switch")
def request_preview_switch():
    VIDEO.preview = not VIDEO.preview
    print("*"*10, VIDEO.preview)
    return "nothing"


@application.route("/request_flipH_switch")
def request_flipH_switch():
    VIDEO.flipH = not VIDEO.flipH
    print("*"*10, VIDEO.flipH)
    return "nothing"


@application.route("/request_model_switch")
def request_model_switch():
    VIDEO.detect = not VIDEO.detect
    print("*"*10, VIDEO.detect)
    return "nothing"


@application.route("/request_exposure_down")
def request_exposure_down():
    VIDEO.exposure -= 1
    print("*"*10, VIDEO.exposure)
    return "nothing"


@application.route("/request_exposure_up")
def request_exposure_up():
    VIDEO.exposure += 1
    print("*"*10, VIDEO.exposure)
    return "nothing"


@application.route("/request_contrast_down")
def request_contrast_down():
    VIDEO.contrast -= 4
    print("*"*10, VIDEO.contrast)
    return "nothing"


@application.route("/request_contrast_up")
def request_contrast_up():
    VIDEO.contrast += 4
    print("*"*10, VIDEO.contrast)
    return "nothing"


@application.route("/reset_camera")
def reset_camera():
    STATUS = reset_settings()
    print("*"*10, STATUS)
    return "nothing"


if __name__ == "__main__":
    application.run(debug=True)
