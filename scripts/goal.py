import rospy
import  move_base_msgs.msg
import  tf
import  actionlib
from actionlib_msgs.msg import *
import math

'''
    right-top
  pose:
    position:
      x: -5.71431815236
      y: -8.40889293448
      z: 0.0
    orientation:
      x: 0.0
      y: 0.0
      z: -0.713712599795
      w: 0.700438666047


left-bottom
pose:
  pose:
    position:
      x: -18.7830073854
      y: -19.2417090815
      z: 0.0
    orientation:
      x: 0.0
      y: 0.0
      z: 0.544106422732
      w: 0.839016210059

'''


def gotoGoalEuler(x, y, theta) :
    quaternion = tf.transformations.quaternion_from_euler(0, 0, theta)
    goal = move_base_msgs.msg.MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = quaternion[2]
    goal.target_pose.pose.orientation.w = quaternion[3]

    gotoGoal(goal)

def gotoGoalQuaternion(x, y, z, w) :
    goal = move_base_msgs.msg.MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

    gotoGoal(goal)

def gotoGoal(goal) :
    action = actionlib.SimpleActionClient('move_base', move_base_msgs.msg.MoveBaseAction)
    action.wait_for_server()
    state = GoalStatus.ABORTED
    action.send_goal(goal)
    while state != GoalStatus.SUCCEEDED :
        result = action.wait_for_result(rospy.Duration(0.1))
        state = action.get_state()
        rospy.loginfo("state : " + str(state))

        '''
          PENDING = 0
          ACTIVE = 1
          PREEMPTED = 2
          SUCCEEDED = 3
          ABORTED = 4
          REJECTED = 5
          PREEMPTING = 6
          RECALLING = 7
          RECALLED = 8
          LOST = 9
        '''

        if state == GoalStatus.SUCCEEDED :
            rospy.loginfo("goto goal succeeded (" + str(result) +")")


if __name__ == "__main__" :
    rospy.init_node('simple_goal_python')
    #gotoGoalQuaternion(-5.71, -8.40, -0.713, 0.700)
    gotoGoalQuaternion(14.8281615073, -9.95219217192, 0.83112201785, 0.556090092922)
    #gotoGoalEuler(-5, -8, 45 * math.pi / 180.0)
