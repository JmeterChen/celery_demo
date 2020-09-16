# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-16

from datetime import timedelta
from celery import Celery
# from celery.schedules import crontab


broker = 'redis://127.0.0.1:6379/3'
backend = 'redis://127.0.0.1:6379/4'

app = Celery('my_task2', broker=broker, backend=backend, include=[
	'schedule_demo2.tasks'
])
app.conf.timezone = 'Asia/Shanghai'
app.conf.enable_utc = False

app.conf.beat_schedule = {
    # 名字随意命名
    'add-every-6-seconds': {
        # 执行tasks1下的test_celery函数
        'task': 'schedule_demo2.tasks.push_msg',
        # 每隔2秒执行一次
        # 'schedule': 1.0,
        # 'schedule': crontab(minute="*/1"),
        'schedule': timedelta(seconds=6)
    },
    # 'add-every-12-seconds': {
    #     'task': 'celery_tasks.task01.send_email',
    #     每年4月11号，8点42分执行
    #     'schedule': crontab(minute=42, hour=8, day_of_month=11, month_of_year=4),
    #     'args': ('张三',)
    # },
}