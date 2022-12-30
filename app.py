# -*- coding: utf-8 -*-
import time
import chunk


def change_chunk(cl: list, Ch: chunk.Chunk):
    """
    更改
    :param cl: 输入区块
    :param Ch: 区块所在类
    :return: 列表(新)
    """
    chunk_out = []
    x_length = len(cl[0])
    y_length = len(cl)
    for y_runner in range(0, y_length):
        y_runner_get = cl[y_runner]
        new_chunk_row = []
        for x_runner in range(0, x_length):
            if y_runner_get[x_runner] == 1:
                if Ch.get_per_sum(x_runner, y_runner) <= 2:
                    new_chunk_row.append(0)
                elif Ch.get_per_sum(x_runner, y_runner) == 3:
                    new_chunk_row.append(1)
                elif Ch.get_per_sum(x_runner, y_runner) >= 4:
                    new_chunk_row.append(0)
            else:
                # 此之谓死
                if Ch.get_per_sum(x_runner, y_runner) >= 3:
                    new_chunk_row.append(1)
                else:
                    new_chunk_row.append(0)
        chunk_out.append(new_chunk_row)

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
        main_chunk.set_item_org(a[0], a[1])
    print("即将开始循环")
    print("信息:", t_slp, circle)
    num = 0
    while True:
        time.sleep(t_slp)
        num += 1
        print_chunk(main_chunk.chunk, num)
        new_chunk = change_chunk(main_chunk.chunk, main_chunk)
        main_chunk.chunk_update(new_chunk)
        if num >= circle:
            print("循环结束, 即将退出")
            input("按回车退出")
            exit(0)
