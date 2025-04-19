#FROM ubuntu:latest
#LABEL authors="Lenovo"
#
#ENTRYPOINT ["top", "-b"]


# 使用官方 Python 基础镜像
FROM python:3.10

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY . /app

# 安装依赖
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 8002

# 运行 Django 项目
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]