# -*- coding:utf-8 -*-
import time
import app

"""
介绍: 生命游戏(Life Game)
作者: 成昊天
Github: github.com/chenghaotian
Email: dboycht@qq.com
"""

"""
本文件版本: 1.0
更新日志:
v1.0
    日期: Dec.30/2022
    简短介绍: 首次诞生, 命令行版本
"""

if __name__ == '__main__':
    cg = []
    print("欢迎来到生命游戏 v1.0 \n"
          "作者: 成昊天\n"
          "注意: 横轴正方向向右, 纵轴正方向向下")
    x1 = int(input("请输入横向长度:"))
    y1 = int(input("请输入纵向长度:"))
    t_sl = float(input("下面请输入刷新时间间隔(请输入浮点数):"))
    cir = int(input("下面请输入迭代次数:"))
    print("下面即将输入赐予生命坐标, 直接按回车退出, 输入的坐标为计算机坐标")
    time.sleep(0.05)
    while True:
        xx = input("横轴坐标:")
        if xx == "":
            break
        xx = int(xx)
        yy = int(input("纵轴坐标:"))
        cg.append([xx, yy])
    go = app.main(x1, y1, t_sl, cg, cir)
