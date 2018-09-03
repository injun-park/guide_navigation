#!/usr/bin/env python

import rospy 
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from guide_navigation.srv import *

locations = [
  [(421, "정보기술연구소"), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 1.0)],
  [(422, "test"), (1.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)]
]

client  = ''

def goal_pose(pose):
  goal_pose = MoveBaseGoal()
  goal_pose.target_pose.header.frame_id = 'map'
  goal_pose.target_pose.pose.position.x = pose[1][0]
  goal_pose.target_pose.pose.position.y = pose[1][1]
  goal_pose.target_pose.pose.position.z = pose[1][2]
  goal_pose.target_pose.pose.orientation.x = pose[2][0]
  goal_pose.target_pose.pose.orientation.y = pose[2][1]
  goal_pose.target_pose.pose.orientation.z = pose[2][2]
  goal_pose.target_pose.pose.orientation.w = pose[2][3]

  return goal_pose

def service_req(req):

  for pose in locations :
    if pose[0][0] == req.location:
      goal = goal_pose(pose)
      client.send_goal(goal)
      client.wait_for_result()
    else : 
      return GuideNavigationResponse("couldn't found location")

if __name__ == '__main__':
  rospy.init_node('guide_navigation')

  client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
  client.wait_for_server()

  service = rospy.Service('guide_navigation', GuideNavigation, service_req)

  rospy.spin()

