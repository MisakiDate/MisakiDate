"""
Run once daily at 08:00 local time using APScheduler.

Usage:
    python scheduler.py
"""

from apscheduler.schedulers.blocking import BlockingScheduler

from email_sender import send_daily_quote

scheduler = BlockingScheduler()


@scheduler.scheduled_job("cron", hour=8, minute=0)
def job():
    send_daily_quote()


if __name__ == "__main__":
    print("Scheduler started — daily quote will be sent at 08:00.")
    scheduler.start()
