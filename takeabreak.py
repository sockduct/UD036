# Imports
import time
import webbrowser

# Variables
loops = 3
sleepsecs = 5
youtubevideo = 'd-v1lCU4NoU'
youtubesite = 'www.youtube.com'
youtubewatch = '/watch?v='
webaccess = 'https://'

# Main
count = 0

starttime = time.time()
print "Take a break began at " + time.ctime()
# Another stylistic option:
# while(count < loops):
while count < loops:
    time.sleep(sleepsecs)
    webstring = webaccess + youtubesite + youtubewatch + youtubevideo
    webbrowser.open(webstring)
    count += 1
endtime = time.time()
duration = endtime - starttime
print "Program ended at " + time.ctime()
print "Program run for " + str(duration) + " seconds."

