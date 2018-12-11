#!/usr/bin/python
# -*- coding: utf-8 -*-  
from core_tool import *
def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
  t1=4
  t2=1

  def quaternion(axis,angle) :
	return [i*math.sin(angle/2) for i in axis]+[math.cos(angle/2)]

  #基本情報  
  q1 = quaternion([0,1,0],math.pi)
  q2 = quaternion([0,0,1],math.pi/2)
  q3 = list(MultiplyQ(q1,q2))

  x1=0.5 #最初に拾うジェンガの中心座標
  y1=0.1
  z1=0.295

  x2=0.3 #最初に置く段の真ん中のジェンガの中心座標
  y2=-0.2
  z2=0.295
  
  thick=0.075
  h=0.015
  w=0.025

  def pickup(a): #ジェンガを所定位置から拾う
   ct.robot.MoveToX([x1,y1+a*w,z1+0.1]+q3,t1,blocking=True) 
   rospy.sleep(t2)
   ct.robot.OpenGripper()
   rospy.sleep(t2)
   ct.robot.MoveToXI([x1,y1+a*w,z1]+q3,t1,blocking=True)#一回ごとにwだけｙ軸側に拾う位置をずらします
   rospy.sleep(t2)
   ct.robot.MoveGripper(thick)
   rospy.sleep(t2)
   ct.robot.MoveToXI([x1,y1+a*w,z1+0.1]+q3,t1, blocking=True)
   rospy.sleep(t2)

#段が変わるごとに置く位置をz軸方向にhだけずらします
  def move1(a,b):#姿勢１の状態で積む位置に移動し置く
   ct.robot.MoveToX([x2+w*a,y2,z2+0.1+2*b*h]+q1,t1,blocking=True)#同じ段では一回ごとにwだけx軸に沿って置く位置をずらします
   rospy.sleep(t2)
   ct.robot.MoveToXI([x2+w*a,y2,z2+2*b*h]+q1,t1,blocking=True) 
   rospy.sleep(t2)
   ct.robot.OpenGripper()
   rospy.sleep(t2)
   ct.robot.MoveToXI([x2+w*a,y2,z2+0.1+2*b*h]+q1,t1,blocking=True) 
   rospy.sleep(t2)

  def move3(a,b): #姿勢３の状態で積む位置に移動し置く
   ct.robot.MoveToX([x2,y2+w*a,z2+0.1+(1+2*b)*h]+q3,t1,blocking=True)#同じ段では一回ごとにwだけy軸に沿って置く位置をずらします
   rospy.sleep(t2)
   ct.robot.MoveToXI([x2,y2+w*a,z2+(1+2*b)*h]+q3,t1,blocking=True) 
   rospy.sleep(t2)
   ct.robot.OpenGripper()
   rospy.sleep(t2)
   ct.robot.MoveToXI([x2,y2+w*a,z2+0.1+(1+2*b)*h]+q3,t1,blocking=True) 
   rospy.sleep(t2)

  def moveq1():
   ct.robot.MoveToQ([2.6275370439141383, -0.31581660711503085, -2.4742835903093434, -1.4535463123185441, -2.9464209645350925, 1.4393073683000435, 1.4161135201399193],t1,blocking=True)#元の位置に戻ります
   rospy.sleep(t2)


  def move0():
   ct.robot.MoveToQ([-0.02225359399919708, 0.027608916799549812, 0.022566861740566175, -2.2001428621168677, -0.00047802839581177894, 0.6569213757903858, 0.0010121492739857683],t1,blocking=True)#元の位置に戻ります
   rospy.sleep(t2)

#ここから実行
  move0()
  for k in range(2):#とりあえず４段積むことにしました
   for i in range(3):
    pickup(6*k+i)
    move1(i-1,k)
    moveq1()
   for j in range(3):
    pickup(6*k+3+j)
    move3(j-1,k)
    moveq1()
  move0()
#拾うジェンガはx軸に平行な姿勢でx１，y１，z１座標からy軸に沿ってy軸正方向に向かって並べます
