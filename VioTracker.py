import random
import numpy
import datetime

class VioTracker:
    def __init__(self, frames_per_video = 7):
        self.frames_per_video = frames_per_video
        pass

    def check_violation(self, frame):
        r =random.random()
        if r > 0.8 :
            return True
        return False

    def get_description(self):
        desc = {
            "Drove with no helmet" : 2,
            "More than one driver" : 4,
            "Cross in red light" : 5,
            "Doesn't stop in stop sign" : 5,
            "Drove on sidewalk" : 4,
            "Drove not in right lane" : 5,
        }
        violation = random.choice(list(desc))
        return [violation, desc[violation], datetime.datetime.now()]


    def get_face_location(self):
        top_right_x = random.randint(0,800)
        top_right_y = random.randint(0,800)
        bottom_left_x = top_right_x + 200
        bottom_left_y = top_right_y + 200


        face_location = [
            top_right_x,
            top_right_y,
            bottom_left_x,
            bottom_left_y
        ]
        return face_location

    def get_video(self):
        # video = []
        # for i in range(self.frames_per_video):
        #     frame = numpy.random
        video = numpy.random.rand(self.frames_per_video, 1048,1048)
        return video*100