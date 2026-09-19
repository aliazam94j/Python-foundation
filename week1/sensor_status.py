# Task: Simulate a sensor status check.
#
# Pick a numeric value (e.g. a temperature or pressure reading — hardcode
# it or read it with input()), then use if/elif/else to print one of:
#   "OK"       - value is within a normal range
#   "warning"  - value is getting close to a limit
#   "critical" - value is past the limit
#
# Decide on your own thresholds (e.g. OK < 70, warning 70-90, critical > 90).
#
# Notes coming from C:
# - elif, not "else if".
# - No switch/case in Python (until you learn match/case later) —
#   if/elif/else is the standard tool here.


x =float(input("enter temp "))

if x < 70:
    print("We are good")
elif x < 90:
    print("warning")
else:
    print("Critical")
