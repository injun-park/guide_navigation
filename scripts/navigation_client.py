#!/usr/bin/env python

import sys
import rospy
from guide_navigation.srv import *

def navigation_service_request(location_number):
  rospy.wait_for_service('guide_navigation')
  try:
    client = rospy.ServiceProxy('guide_navigation', GuideNavigation)
    response = client(location_number)
    return response.result
  except rospy.ServiceException, e:
    print "Service call failed: %s"%e

def usage():
    return "%s [location number]"%sys.argv[0]

if __name__ == "__main__":
  if len(sys.argv) == 2:
    location_number = int(sys.argv[1])
  else:
    print usage()
    sys.exit(1)
  print "request location %s"%(location_number)
  print "result %s"%(navigation_service_request(location_number))
