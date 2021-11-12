from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import get_news, get_standings, get_races


def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(get_news, 'interval', minutes=2, jitter=60)
    # scheduler.add_job(get_standings, 'interval', minutes=4, jitter=60)
    # scheduler.add_job(get_races, 'interval', minutes=6, jitter=60)
    scheduler.start()