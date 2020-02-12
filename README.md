# Real-time object detection application

Web application for *real-time* object detection on video streaming via web browser. 


## Installation

Create and activate an virtual environment, as follows:

```bash
$ cd cloned/directory/
$ python -m venv env
$ env/Scripts/activate
```

After have installed and activated the environment, install all the dependencies:

```bash
$ pip install -r requirements.txt
```

After that, you can run the *following command* and access the application at [127.0.0.1:5000](http://127.0.0.1:5000/) on your browser.

```bash
$ python application.py
```

*obs.: This application was tested only on *Google Chrome*.*

## Usage

- **Camera preview**: Enables and disables the webcam preview.
- **Run detection model**: Enables and disables the detection model.
- **Exposure**: Buttons which increase or decrease camera exposure stops by 1.
- **Contrast**: Buttons which increase or decrease camera contrast stops by 4.
- **Reset camera**: Reset all camera settings based on *camera_settings.log* file.