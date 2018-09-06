import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image

class Zed_img:
    def __init__(self):
        self.bridge = cv_bridge.CvBridge()
        cv2.namedWindow("window",1)
        self.image_sub = rospy.Subscriber('/zed/left/image_rect_color', Image, self.image_callback)
    def image_callback(self,msg):
        image = self.bridge.imgmsg_to_cv2(msg)
        cv2.imshow("window", image)
        cv2.waitKey(3)

rospy.init_node('zed_img')
zed_img = Zed_img()
rospy.spin()