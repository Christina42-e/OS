import schedule
import time

def send_notification():
    print("This is your scheduled notification")

# Schedule the notification every 10 seconds
schedule.every(10).seconds.do(send_notification)

print("Scheduler started. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)