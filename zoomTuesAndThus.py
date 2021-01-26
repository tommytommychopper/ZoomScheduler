import webbrowser
from datetime import datetime

# Get current time
current_time = datetime.now().strftime('%H:%M')

# Tuesday and Thursday Classes
# CSCI 430 (Lecture)        4:00AM
# CSCI 430 (Activity)       5:00AM
# CSCI340(Lecture)          6:00AM
# CSCI567                   9:00AM

if(current_time == '04:00'):
    webbrowser.open('URL')

if(current_time == '05:00'):
    webbrowser.open('URL')

if(current_time == '06:00'):
    webbrowser.open('URL')
if(current_time == '09:00'):
    webbrowser.open('URL')
