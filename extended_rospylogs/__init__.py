import sys, os
import rospy

def log_cond(cond, msg, logfunction, *args, **kwargs):
    if type(cond) != bool:
        raise TypeError("First arguemnt needs to be boolean -> Received: {}".format(type(cond)))
    if cond:
        append_name = kwargs.pop('show_name', True)
        if append_name:
            name = rospy.get_name().split("/")[-1] #get name and remove "/"
            msg = "[" + name.upper() + "] " + nmsg
        logfunction(msg, *args, **kwargs)

def logdebug_cond(cond, msg, *args, **kwargs):
    log_cond(cond, msg, rospy.logdebug, *args, **kwargs)

def loginfo_cond(cond, msg, *args, **kwargs):
    log_cond(cond, msg, rospy.loginfo, *args, **kwargs)

def logwarn_cond(cond, msg, *args, **kwargs):
    log_cond(cond, msg, rospy.logwarn, *args, **kwargs)

def logerr_cond(cond, msg, *args, **kwargs):
    log_cond(cond, msg, rospy.logerr, *args, **kwargs)

def logfatal_cond(cond, msg, *args, **kwargs):
    log_cond(cond, msg, rospy.logfatal, *args, **kwargs)
