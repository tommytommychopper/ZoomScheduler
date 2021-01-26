import webbrowser
from datetime import datetime


# Get current time
current_time = datetime.now().strftime('%H:%M')

# Tuesday and Thursday Classes
# CSCI340(Lecture)          6:00AM
# CSCI300                   7:00AM

if(current_time == '06:00'):
    webbrowser.open('URL')

if(current_time == '07:00'):
    webbrowser.open('URL')
