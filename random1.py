import random
import pyautogui
import time

# 定义每个数字对应的点击位置（x, y）
click_positions = {
    '0':  (983, 984),
    '1': (819, 753),
    '2': (956, 753),
    '3': (1143, 762),
    '4': (835, 821),
    '5': (969, 836),
    '6':(1116, 828),
    '7': (829, 877),
    '8': (935, 899),
    '9':(1089, 900)
}

# 生成四个随机数字
random_digits = ''.join(str(random.randint(0, 9)) for _ in range(4))
# print(f"随机生成的数字: {random_digits}")

# 延迟几秒钟，以便您可以切换到目标窗口
time.sleep(5)

# 根据每个数字的值去点击对应位置
for index,digit in enumerate(random_digits):
    for i in range(len(random_digits)):
        position = click_positions[digit]
        offset_x = random.randint(-5, 5)  # 在-5到5之间随机选择x偏移
        offset_y = random.randint(-5, 5)  # 在-5到5之间随机选择y偏移

        # 应用偏移
        adjusted_position = (position[0] + offset_x, position[1] + offset_y)

        # 执行点击
        pyautogui.click(adjusted_position)  # 点击调整后的位置
    #     # if index==2:
    #     #     break
    #     # print(f"点击位置: {position}")  # 输出点击位置
        time.sleep(random.uniform(2, 3))  # 随机暂停2-3秒之间
        break
time.sleep(5)


pyautogui.click((1563, 1060))
time.sleep(2)
pyautogui.click((1563, 1060))
time.sleep(2)

# # 根据每个数字的值去点击对应位置
for digit in random_digits:
    for i in range(len(random_digits)):
        position = click_positions[digit]
        offset_x = random.randint(-5, 5)  # 在-5到5之间随机选择x偏移
        offset_y = random.randint(-5, 5)  # 在-5到5之间随机选择y偏移

        # 应用偏移
        adjusted_position = (position[0] + offset_x, position[1] + offset_y)

        # 执行点击
        pyautogui.click(adjusted_position)  # 点击调整后的位置
    #     # if index==2:
    #     #     break
    #     # print(f"点击位置: {position}")  # 输出点击位置
        time.sleep(random.uniform(2, 3))  # 随机暂停2-3秒之间
        break