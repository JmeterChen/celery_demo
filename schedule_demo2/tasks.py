# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-16


from schedule_demo.celery import app
import time


@app.task
def push_msg():
	time.sleep(5)
	print("恭喜房多多上市成功222222！！！")
	return True