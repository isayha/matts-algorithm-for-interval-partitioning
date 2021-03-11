# Assignment 4
# Part 2 (Python Source Code)
# CPSC 482
# Isayha Raposo
# Student Number: 230133508

import sys
from files import *
from tabulate import tabulate # Requires package "tabulate" (pip install tabulate)
from datetime import time # Requires package "datetime" (pip install datetime)

# Handles data retrieval (see files.py)
data = getData(sys.argv)

# Processes input data (Obtains the specified lecture start/finish times):
lectures = []
lectureCount = 0
dataLine = data.readline().strip('\n')
while not (dataLine == ""):
    lectureCount += 1
    try:
        times = [int(time) for time in dataLine.split("-")]
        if len(times) != 2:
            raise Exception()
        elif times[0] >= times[1]:
            raise Exception()
        for original_time in times:
            converted_time = time(int(original_time/100), int(original_time%100), 0) # Used to check if times are valid
    except:
        handleDataIssue(True, ("Line " + str(lectureCount) + " of data file incorrectly formatted or invalid."))
    lectures.append(times)
    dataLine = data.readline().strip('\n')

# Sort input data:
def getStartTime(lecture):
    return lecture[0]
lectures.sort(key=getStartTime)

# Algorithm:
def lectureIsCompatible(lecture, classroom):
    if lecture[0] >= classroom[-1][1]:
    # If the starting time of the given lecture is greater than or equal to
    # the end time of the lecture last appended to the given classroom...
        return True
    return False

classrooms = []
while lectures:
    incompatible_lectures = []
    classroom = []
    classroom.append(lectures[0])
    lectures.pop(0)
    for lecture in lectures:
        if lectureIsCompatible(lecture, classroom):
            classroom.append(lecture)
        else:
            incompatible_lectures.append(lecture)
    classrooms.append(classroom)
    lectures = incompatible_lectures

# Format output data:
formatted_classrooms = []
for classroom in classrooms:
    formatted_classroom = []
    for lecture in classroom:
        formatted_lecture = str(lecture[0]) + "-" + str(lecture[1])
        formatted_classroom.append(formatted_lecture)
    formatted_classrooms.append(formatted_classroom)

# Print output data:
print(tabulate(enumerate(formatted_classrooms), headers=["Classroom:", "Lectures:"]))