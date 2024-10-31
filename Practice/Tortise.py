# import math
#
# def race(v1, v2, g):
#     if v2 <= v1:
#         return [-1,-1,-1]
#     time_in_hours = g/(v2-v1)
#
#     hours = math.floor(time_in_hours)
#     minutes = math.floor((time_in_hours - hours) * 60)
#     seconds = math.floor((time_in_hours - hours) * 3600)
#
#     return [hours,minutes,seconds]
#
# result = (720,850,70)
# print(result)
#
# import sys
# print(sys.version_info)
# print(sys.version)
from operator import itemgetter


def array_diff(a, b):
    for i in range(len(b)):
        if b[i] in a:
            a.remove(b[i])

    return a


