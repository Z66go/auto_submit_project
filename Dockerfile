# 1. 使用官方提供的、自带浏览器的 Python 镜像（省去在容器里装 Chrome 的麻烦）
FROM mcr.microsoft.com/playwright/python:v1.50.0-jammy

# 2. 设置容器内的工作目录
WORKDIR /app

# 3. 复制依赖文件并安装第三方库（如 pytest, playwright）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 把本地项目的所有代码复制到容器的 /app 目录下
COPY . .

# 5. 容器启动时，自动运行测试命令（--headless 表示在无界面模式下运行，防止报错）
CMD ["pytest", "tests/test_submit.py", "-v"]