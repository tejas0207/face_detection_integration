from datetime import datetime
import pywhatkit

now = datetime.now()
hours = int(now.strftime("%H"))
type_hour = type(hours)
print(type_hour)
print("Current Time =", hours)
minutes = int(now.strftime("%M")) + 1
type_minutes = type(minutes)
print(type_minutes)
print("Current Time =", minutes)


pywhatkit.sendwhatmsg("" , "Hey bud ,  we have completed the task ",hours,minutes)