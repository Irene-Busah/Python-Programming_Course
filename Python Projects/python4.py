import time

# countdown timer

def countdown(seconds):

    while seconds:
        minutes, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print('Done')
seconds = input('Enter time in seconds: ')

countdown(int(seconds))
