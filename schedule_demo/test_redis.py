# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-16


import redis
import json


# r = redis.Redis(host="127.0.0.1", port=6379, db=1)
r = redis.Redis(host="10.50.255.104", port=6379, db=13)
# redis://10.50.255.104:6379/3


# for i in r.lrange("celery", 0, -1):
#
# 	print(i)
key_list = r.keys()
reallyresult = []
for i in key_list:
	print(i)
	i = str(i, encoding='utf-8').replace("true", "True").replace(
		"null", "None").replace("false", "False").replace("\\xa0", " ")
	# print(i)
	# print(r.get(i))
	res = str(r.get(i), encoding='utf-8').replace("true", "True").replace(
		"null", "None").replace("false", "False").replace("\\xa0", " ")
	# print(type(res))
	res = eval(res)
	if res["status"] != "SUCCESS":
		continue
	else:
		print(res)
# print(r.get("celery-task-meta-7804df68-d97a-4761-9261-92949878749d"))