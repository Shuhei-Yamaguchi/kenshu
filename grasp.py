#!/usr/bin/python
# -*- coding: utf-8 -*-  
from core_tool import *
def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
  t1=8.0
  t2=2.0
  #ct.robot.MoveToQ([-0.022252655408980263, 0.027614737576572786, 0.022566458144161798, -2.2001402673293486, -0.000479466881727285, 0.6569522371938831, 0.001012663271254672], t1,blocking=True) #moveq 1と同義です
  #rospy.sleep(t2)
  x=0.5
  y=0.1
  z=0.19
  thick=0.05
  ct.robot.MoveToX([0.4, y, z, 0.0, 0.70709699483067157, 0.0, 0.70711656736701733],t1, blocking=True)
  rospy.sleep(t2)
  ct.robot.MoveToX([x, y, z, 0.0, 0.70709699483067157, 0.0, 0.70711656736701733],3.0,blocking=True) #目標物のｘ，ｙ，ｚ座標を狙って移動します
  rospy.sleep(t2)
  ct.robot.OpenGripper()#グリッパーを全開
  rospy.sleep(t2)
  ct.robot.MoveGripper(thick)#目標物をはさみます
  rospy.sleep(t2)
  ct.robot.MoveToQ([-0.022252655408980263, 0.027614737576572786, 0.022566458144161798, -2.2001402673293486, -0.000479466881727285, 0.6569522371938831, 0.001012663271254672], t1,blocking=True)#元の位置に戻ります
