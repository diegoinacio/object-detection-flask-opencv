"""
This script downloads the weight file
"""
import requests

URL = "https://pjreddie.com/media/files/yolov3.weights"
r = requests.get(URL, allow_redirects=True)
open('yolov3_t.weights', 'wb').write(r.content)
