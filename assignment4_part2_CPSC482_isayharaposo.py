# Assignment 4
# Part 2 (Python Source Code)
# CPSC 482
# Isayha Raposo
# Student Number: 230133508

import sys
from files import *

# Handles data retrieval (see files.py)
data = getData(sys.argv)

# Processes input data (Obtains the specified lecture start/finish times):
lectures = []
lectureCount = 0
dataLine = data.readline().strip('\n')
while not (dataLine == ""):
    lectureCount += 1
    try:
        lectures.append([int(time) for time in dataLine.split(", ")])
    except:
        handleDataIssue(True, ("Line " + str(lectureCount) + " of data file incorrectly formatted."))
    dataLine = data.readline().strip('\n')

# Algorithm:
print(lectures) #test
        
    