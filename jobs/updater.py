from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import get_news, get_standings, get_races


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_news, "interval", minutes=10, jitter=60)
    scheduler.add_job(get_standings, "interval", minutes=15, jitter=60)
    scheduler.add_job(get_races, "interval", hours=1, jitter=120)
    scheduler.start()
