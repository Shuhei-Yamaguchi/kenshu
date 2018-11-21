#!/usr/bin/python
# -*- coding: utf-8 -*-  
from core_tool import *
def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
  t=2.0
  ct.robot.MoveToQ([-0.022252655408980263, 0.027614737576572786, 0.022566458144161798, -2.2001402673293486, -0.000479466881727285, 0.6569522371938831, 0.001012663271254672], t) #moveq 1と同義です
  rospy.sleep(t)
  x=0.45000971329610545
  y=0.33
  z=0.5
  ct.robot.MoveToX([x, y, z, 0.0, 0.70709699483067157, 0.0, 0.70711656736701733],t) #目標物のｘ，ｙ，ｚ座標を狙って移動します
  rospy.sleep(t)
  ct.robot.OpenGripper()#グリッパーを全開
  rospy.sleep(t)
  ct.robot.MoveGripper(0.5)#目標物をはさみます
  rospy.sleep(t)
  ct.robot.MoveToQ([-0.022252655408980263, 0.027614737576572786, 0.022566458144161798, -2.2001402673293486, -0.000479466881727285, 0.6569522371938831, 0.001012663271254672], t)#元の位置に戻ります
  print ct
