# -*- coding: utf-8 -*-
import time
import chunk


def change_chunk(chunk_in: chunk.Chunk):
    chunk_out = []
    x_len = chunk_in.x
    y_len = chunk_in.y
    for yi in range(0, y_len):
        row = []
        for xi in range(0, x_len):
            if chunk_in.get_item(xi, yi) == 0:
                if chunk_in.get_per_sum(xi, yi) >= 3:
                    row.append(1)
                else:
                    row.append(0)
            else:
                if chunk_in.get_per_sum(xi, yi) < 4:
                    row.append(0)
                else:
                    row.append(1)
        chunk_out.append(row)
    return chunk_out


def print_chunk(chunk_input: list, no_n: int):
    """
    输出区块
    :param chunk_input:区块
    :param no_n:循环圈次数
    :return: 啥也没有
    """
    blocks = ["□", "■"]
    print("")
    print(f"当前迭代数: 第{no_n}次")
    for hand in chunk_input:
        for i in hand:
            print(blocks[i], end="")
        print("")


def main(x: int, y: int, t_slp: float, chg_l: list, circle: int):
    """
    主程序
    :param x: 横轴长度
    :param y: 纵轴长度
    :param t_slp: 刷新时间
    :param chg_l: 生命坐标
    :param circle: 循环迭代次数
    :return: 啥也没有
    """
    main_chunk = chunk.Chunk(x, y)
    for a in chg_l:
        # 赋予生命
        main_chunk.set_item(a[0], a[1], True)
    print("即将开始循环")
    print("信息:", t_slp, circle)
    num = 0
    while True:
        time.sleep(t_slp)
        num += 1
        print_chunk(main_chunk.chunk, num)
        cc = change_chunk(main_chunk)
        main_chunk.chunk_update(cc)
        if num >= circle:
            print("循环结束, 即将退出")
            input("按回车退出")
            exit(0)
