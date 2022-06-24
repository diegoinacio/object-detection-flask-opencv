"""
This script downloads the weight file
"""
import requests

URL = "https://pjreddie.com/media/files/yolov3.weights"
r = requests.get(URL, allow_redirects=True)
open('yolov3.weights', 'wb').write(r.content)
