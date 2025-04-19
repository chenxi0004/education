#FROM ubuntu:latest
#LABEL authors="Lenovo"
#
#ENTRYPOINT ["top", "-b"]



# 使用官方 Python 镜像
FROM python:3.10

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . /app

# 安装依赖
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 8000

# 运行 Django 项目（假设 manage.py 在项目根目录）
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]