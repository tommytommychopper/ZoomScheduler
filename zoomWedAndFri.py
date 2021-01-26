import webbrowser
from datetime import datetime

# Get current time
current_time = datetime.now().strftime('%H:%M')

# Tuesday and Thursday Classes
# CSCI 515                  5:30AM
# CSCI 340(Activity)        9:00AM

if(current_time == '05:30'):
    webbrowser.open('URL')

if(current_time == '09:00'):
    webbrowser.open('URL')
