#!/usr/bin/python
# -*- coding: utf-8 -*-  
from core_tool import *
def Help():
	return '''Template of script.
	Usage: template'''
def Run(ct,*args):
	x = list(ct.robot.FK())
	print x
	for i in range(2):
		x1 = copy.deepcopy(x)
		x1[0] += 0.1
		ct.robot.MoveToX(x1, 2.0, blocking = True)
		x1[0] -= 0.1
		ct.robot.MoveToX(x1, 2.0, blocking = True)
		print ct
#aaa
