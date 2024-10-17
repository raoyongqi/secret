from pynput import mouse
import time

# 文件名
output_file = 'coordinates.txt'

# 创建或清空文件
with open(output_file, 'w') as f:
    f.write("记录的鼠标点击坐标:\n")

# 鼠标点击事件处理函数
def on_click(x, y, button, pressed):
    if pressed:
        with open(output_file, 'a') as f:
            f.write(f"坐标: ({x}, {y})\n")  # 记录点击坐标
            print(f"记录坐标: ({x}, {y})")  # 在控制台输出

# 设置鼠标监听器
with mouse.Listener(on_click=on_click) as listener:
    print("请点击鼠标，按 'Esc' 键退出...")
    listener.join()  # 开始监听鼠标事件
