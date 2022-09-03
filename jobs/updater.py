from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import get_news, get_standings, get_races


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_news, "interval", minutes=2)
    scheduler.add_job(get_standings, "interval", minutes=2)
    scheduler.add_job(get_races, "interval", minutes=3)
    scheduler.start()
