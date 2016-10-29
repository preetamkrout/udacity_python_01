import time
import webbrowser

def takeABreak (breaks):
    nextBreakAt = 1;
    while nextBreakAt <= breaks:
        time.sleep(10)
        print("Waited for 10 seconds...")
        nextBreakAt = nextBreakAt + 1
        webbrowser.open("https://www.youtube.com/watch?v=UprcpdwuwCg")

noOfBreaks = 4
takeABreak(noOfBreaks)
