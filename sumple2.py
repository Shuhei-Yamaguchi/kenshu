#!/usr/bin/python
# -*- coding: utf-8 -*-  
from core_tool import *
def Help():
  return '''Template of script.
  Usage: template'''
def Run(ct,*args):
  r = 0.05
  #yz 平面で半径 r の円を描きたい
  x = list(ct.robot.FK())
  x1 = copy.deepcopy(x)
  x1[1] -= r
  ct.robot.MoveToX(x1, 1.0, blocking=True)
  #現在位置を中心としたいので円周に移動
  x_traj = []
  #とりあえず空のリストを作ります
  t_traj = []
  x_traj.append(x1)
  #初期位置を x_traj の最初に追加
  t_traj.append(0.0)
  #t_traj の最初の要素は0
  for i in range(1, 50):
   #ループを回す
   t_traj.append(0.1*i)
   #t_traj へ追加。どうやら点間を 0.1s で動かしたいらしい
   x2 = copy.deepcopy(x)
   x2[1] += -r*math.cos(3.0*0.1*i)
   #円になるように y,z 座標をちょっと動かす
   x2[2] += r*math.sin(3.0*0.1*i)
   x_traj.append(x2)
   #x_traj へ追加
   print t_traj
   #traj がどういう内容になってるか実行時に確認してみてください
   print x_traj
   ct.robot.FollowXTraj(x_traj, t_traj)
   #実行
  print ct
