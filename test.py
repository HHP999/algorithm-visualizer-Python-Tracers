# -*- coding: utf-8 -*-
"""
@FileName：test.py
@Description：C++ 示例的 Python 可视化翻译版
@Author：核知坊, 一个激发创造力的网站: http://www.CoreKSets.cn
@Time：2025/6/7 15:54
"""

from algorithm_visualizer import Array2DTracer, LogTracer, Layout, VerticalLayout, Tracer


class Test:
    def __init__(self):
        # 定义 tracer 对象
        self.array2dTracer = Array2DTracer("Grid")
        self.logTracer = LogTracer("Console")

        # 设置输入数据
        self.messages = [
            "Visualize",
            "your",
            "own",
            "code",
            "here!"
        ]

        # 创建 layout 对象
        root_layout = VerticalLayout([self.array2dTracer, self.logTracer])
        Layout.set_root(root_layout)  # 使用实例调用

        # 设置 Array2D 的数据
        self.array2dTracer.set(self.messages)
        Tracer.delay()

        # 开始可视化递归高亮
        self.highlight(0)

    def highlight(self, line):
        if line >= len(self.messages):
            return

        message = self.messages[line]

        # 可视化逻辑
        self.logTracer.println(message)
        self.array2dTracer.selectRow(line, 0, len(message) - 1)
        Tracer.delay()
        self.array2dTracer.deselectRow(line, 0, len(message) - 1)

        # 递归处理下一行
        self.highlight(line + 1)


# 主入口
if __name__ == "__main__":
    Test()
