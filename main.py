# Following code is intended to each camera installed.
# On an infinite loop, the camera will analize the feed and check for violation.
# If found, the violation will be saved to a short video of 10 frames
# and will be transmitted to a control unit along with other important information.

from CameraFeed import CameraFeed
from VioTracker import VioTracker
from mqttClient import mqttClient
import time


camera = CameraFeed()
violationTracker = VioTracker()
client = mqttClient(client_id=camera.get_camera_name())

# Infinite loop
while True:
    # GET the camera frame
    frame = camera.get_frame()

    # Analize the frames to find trtaffic violations - computer vision
    if violationTracker.check_violation(frame) == True:

        # Gather information
        description = violationTracker.get_description()
        info = {
            "camera_id": camera.get_camera_name(),
            "camera_coordinates": camera.get_location(),
            "time_of_violation": description[2],
            "violation_description": description[0],
            "violation_severety": description[1],
            "face_location_in_frame": violationTracker.get_face_location(),
            "video": violationTracker.get_video(),
        }

        # Send to control
        client.send_data(info)

    time.sleep(2)  # only for demonstration purposes
