# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-09-16


from tasks import *


def do_add(x, y):
	res = add.delay(x, y)
	print(res.id)
	return {"code": 200, "mag": "success"}
	

def registered():
	name = input("请输入注册人员名称：")
	push_email.delay(name)
	return {"code": 200, "msg": f"恭喜{name}注册成功! 请查看邮箱点击确认链接进行校验。"}


if __name__ == '__main__':
	print(do_add(100, 200))
	print(registered())