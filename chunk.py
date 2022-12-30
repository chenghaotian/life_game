# -*- coding: utf-8 -*-
# 区块生成库


class Chunk(object):
    """
    区块矩阵
    """

    def __init__(self, x: int, y: int):
        """
        初始化
        :param x: 矩阵横长
        :param y: 矩阵纵长
        """
        self.x = x
        self.y = y
        self.chunk = []
        row = []
        for i in range(0, self.x):
            row.append(0)
        for i in range(0, self.y):
            self.chunk.append(row)

    def get_chunk(self):
        """
        获得区块
        :return: 区块矩阵 list(list)
        """
        return self.chunk

    def get_item(self, x_get: int, y_get: int):
        """
        获取项值
        :param x_get: 计算机中坐标
        :param y_get: 计算机中坐标
        :return: 项值: int
        """
        x_pra = x_get % self.x
        y_pra = y_get % self.y
        return self.chunk[y_pra][x_pra]

    def get_per_sum(self, x_item: int, y_item: int):
        """
        获取周围的和
        :param x_item: x
        :param y_item: y
        :return: 和:int
        """
        sigma_coo = [
            [x_item, y_item],
            [x_item + 1, y_item],
            [x_item - 1, y_item],
            [x_item, y_item - 1],
            [x_item + 1, y_item - 1],
            [x_item - 1, y_item - 1],
            [x_item, y_item + 1],
            [x_item + 1, y_item + 1],
            [x_item - 1, y_item + 1]
        ]
        sigma = 0
        for item_get in sigma_coo:
            sigma += self.get_item(item_get[0], item_get[1])
        return sigma

    def set_item(self, x_set: int, y_set: int, state: bool):
        """
        设置值
        :param x_set: x
        :param y_set: y
        :param state: 状态
        :return:啥也没有
        """
        fg = []
        for a in range(0, self.y):
            row = []
            if a == y_set:
                for q in range(0, self.x):
                    if q == x_set:
                        row.append(1)
                    else:
                        row.append(0)

            else:
                for q in range(0, self.x):
                    if self.chunk[a][q] == 0:
                        row.append(0)
                    else:
                        row.append(1)

            fg.append(row)
        self.chunk_update(fg)

    def chunk_update(self, new: list):
        self.chunk = new
