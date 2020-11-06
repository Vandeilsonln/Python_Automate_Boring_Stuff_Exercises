#! python3
# countdown.py - A simple countdown script.

import time, subprocess, webbrowser


timeLeft = 10

while timeLeft > 0:
    print(timeLeft, end=', ')
    time.sleep(1)
    timeLeft -= 1

subprocess.Popen(['start', webbrowser.open('https://www.youtube.com/watch?v=x5Clu5Rif2U&ab_channel=Lu%C3%ADsKalil')])