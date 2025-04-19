from PIL import Image, ImageDraw
import random


def generate_avatar(filename):
    # 创建一个 200x200 的空白图像
    image = Image.new(
        "RGB",
        (200, 200),
        color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    )
    draw = ImageDraw.Draw(image)

    # 绘制一个圆形作为头像
    draw.ellipse(
        (50, 50, 150, 150),
        fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    )

    # 随机选择眼睛位置
    eye_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.ellipse((70, 70, 90, 90), fill=eye_color)  # 左眼
    draw.ellipse((110, 70, 130, 90), fill=eye_color)  # 右眼

    # 随机选择鼻子位置
    nose_color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )
    draw.line((100, 90, 100, 110), fill=nose_color, width=2)

    # 随机选择嘴巴位置
    mouth_color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )
    draw.arc((70, 110, 130, 130), start=0, end=180, fill=mouth_color, width=2)

    # 保存图像
    image.save(filename)


# 生成 50 张头像
for i in range(50):
    generate_avatar(f"avatar_{i}.png")
# from faker import Faker
# import requests
# import os
#
# fake = Faker()
#
# # 创建保存头像的目录
# if not os.path.exists('avatars'):
#     os.makedirs('avatars')
#
# # 生成50张头像
# for i in range(50):
#     avatar_url = fake.image_url(width=128, height=128)
#     response = requests.get(avatar_url)
#     with open(f'avatars/avatar_{i+1}.png', 'wb') as f:
#         f.write(response.content)
#
# print("50张头像已生成并保存到avatars目录中。")
