#!/usr/bin/python
# -*- coding: utf-8 -*-  
from core_tool import *
def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
  t1=1.0
  t2=1.0

  def quaternion(axis,angle) :
	return [i*math.sin(angle/2) for i in axis]+[math.cos(angle/2)]
  
  q1 = quaternion([0,1,0],math.pi)
  q2 = quaternion([0,0,1],math.pi/2)
  q3 = list(MultiplyQ(q1,q2))
  x=0.5 #ジェンガを拾う場所
  y=0.1
  z=0.2
  thick=0.074

  def pickup(): #ジェンガを所定位置から拾う
   x0 = list(ct.robot.FK())
   x1 = copy.deepcopy(x0)
   x1[3:] = q1  
   ct.robot.MoveToXI(x1,t1,blocking=True)
   ct.robot.MoveToX([x,y,z+0.1]+q1,t1, blocking=True) #目標物の手前まで移動
   rospy.sleep(t2)
   ct.robot.OpenGripper()#グリッパーを全開
   rospy.sleep(t2)
   ct.robot.MoveToX([x,y,z]+q1,t2, blocking=True)#目標物のｘ，ｙ，ｚ座標を狙って移動します
   rospy.sleep(t2)
   ct.robot.MoveGripper(thick)#目標物をはさみます
   rospy.sleep(t2)
   ct.robot.MoveToX([x,y,z+0.1]+q1,t2, blocking=True) #目標物の手前まで戻る
   rospy.sleep(t2)

  def turn3(): #ジェンガを持った後ｑ３のしせいになる
   x0 = list(ct.robot.FK())
   x1 = copy.deepcopy(x0)
   x1[3:] = q3
   ct.robot.MoveToX(x1,t1,blocking=True)
   rospy.sleep(t2)

  pickup()
  turn3()

  ct.robot.MoveToX([x,y,z]+q3,t2,blocking=True) 
  rospy.sleep(t2)
  ct.robot.OpenGripper()#グリッパーを全開
  rospy.sleep(t2)

  ct.robot.MoveToX(x1,t2,blocking=True)
  rospy.sleep(t2)

  ct.robot.MoveToQ([-0.022252655408980263, 0.027614737576572786, 0.022566458144161798, -2.2001402673293486, -0.000479466881727285, 0.6569522371938831, 0.001012663271254672], t1,blocking=True)#元の位置に戻ります
  rospy.sleep(t2)

  ct.robot.MoveToX(x1,t1,blocking=True)
  rospy.sleep(t2)

  ct.robot.OpenGripper()#グリッパーを全開
  rospy.sleep(t2)

  ct.robot.MoveToX([x, y, z]+q3,t2,blocking=True) 
  rospy.sleep(t2)
 
  ct.robot.MoveGripper(thick)#目標物をはさみます
  rospy.sleep(t2)

  ct.robot.MoveToX(x1,t2,blocking=True)
  rospy.sleep(t2)

  ct.robot.MoveToX([x,y,z+0.1]+q1,t1, blocking=True) 
  rospy.sleep(t2)

  ct.robot.MoveToX([x,y,z]+q1,t2, blocking=True) 
  rospy.sleep(t2)

  ct.robot.OpenGripper()#グリッパーを全開
  rospy.sleep(t2)

  ct.robot.MoveToX([x,y,z+0.1]+q1,t2, blocking=True) 
  rospy.sleep(t2)

  ct.robot.MoveToQ([-0.022252655408980263, 0.027614737576572786, 0.022566458144161798, -2.2001402673293486, -0.000479466881727285, 0.6569522371938831, 0.001012663271254672], t1,blocking=True)#元の位置に戻ります
