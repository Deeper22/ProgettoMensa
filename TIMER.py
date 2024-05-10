import time

def timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = '{}:{}'.format(mins, secs)
        print(timer_display, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Timer scaduto!")

# Avvia il timer per 0.1 minuto
timer(0.1)
