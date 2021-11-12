from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import get_news, get_standings, get_races


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_news, 'interval', hours=1, jitter=240)
    scheduler.add_job(get_standings, 'interval', hours=2, jitter=300)
    scheduler.add_job(get_races, 'interval', hours=2, jitter=300)
    scheduler.start()