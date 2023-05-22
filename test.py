import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "POMODORO",
            message = "OK",
            timeout = 10
        )
        time.sleep(5)