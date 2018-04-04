import sys, os
import rospy

def logdebug_cond(cond, msg, *args, **kwargs):
    if cond:
        rospy.logdebug(msg, *args, **kwargs)
