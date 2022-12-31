# -*- coding:utf-8 -*-
import time
import app
import random

"""
介绍: 生命游戏(Life Game)
作者: 成昊天
Github: github.com/chenghaotian
Email: dboycht@qq.com
"""

"""
本文件版本: 1.2
更新日志:
v1.0
    日期: Dec.30/2022
    简短介绍: 首次诞生, 命令行版本
v1.1
    日期: Dec.30/2022
    简短介绍: 修复了一个一个bug, 更新了游戏规则
v1.2
    日期: Dec.31/2022
    简短介绍: 更新了游戏规则, 与原版相同, 并且添加了随机模式

"""

if __name__ == '__main__':
    cg = []
    print("欢迎来到康威生命游戏 v1.2 \n"
          "作者: 成昊天\n"
          "Github: github.com/chenghaotian\n"
          "注意: 横轴正方向向右, 纵轴正方向向下, 规则与原版(康威生命游戏)相同\n"
          "游戏规则:\n"
          "     1.有生命的为\'■\', 无生命的为\'□\'\n"
          "     2.无生命的周围若有三个有生命的, 它将会赐予生命, 反之则无\n"
          "     3.有生命的周围若至多有一个有生命的, 它将会夺去生命\n"
          "     4.有生命的周围若有三个或两个有生命的, 它将会保持生命\n"
          "     5.有生命的周围若至少有四个有生命的, 它将会夺去生命\n"
          "     6.规则2 模拟\'繁殖\', 规则3 模拟孤立而死, 规则5 模拟过多而导致的死亡\n"
          "     7.在输入横坐标时按回车退出录入模式\n"
          )
    x1 = int(input("请输入横向长度:"))
    y1 = int(input("请输入纵向长度:"))
    t_sl = float(input("下面请输入刷新时间间隔(请输入浮点数):"))
    cir = int(input("下面请输入迭代次数:"))
    chose = input("请选择赋予生命的模式, 输入对应字母, 默认随机 (A: 手动输入; B: 随机生成) -?>")
    if chose in ["A", "a"]:
        print("下面即将输入赐予生命坐标, 直接按回车退出")
        time.sleep(0.05)
        while True:
            xx = input("横着数第几个-?>")
            if xx == "":
                break
            xx = int(xx)-1
            yy = int(input("竖着数第几个-?>"))-1
            cg.append([xx, yy])
    else:
        s = x1 * y1
        s_life = input(f"请输入将要赋予的生命个数(不高于{s})-?>")
        if int(s_life) >= s:
            print("[Error 114514, Press Enter to Exit]")
        else:
            for x_mom in range(0, int(s_life)):
                cg.append([random.randint(0, x1-1), random.randint(0, y1-1)])
    go = app.main(x1, y1, t_sl, cg, cir)
