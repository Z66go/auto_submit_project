# 简历投递自动化测试框架

## 项目介绍
基于 Pytest + Playwright + Docker 的 Web 自动化测试框架。
用于验证简历投递系统功能，并可作为 AI Agent（领英/Indeed 投递、电商上架）的自动化验证底座。

## 技术栈
- Python / Flask
- Pytest / Playwright
- Docker

## 本地运行
```bash
pip install -r requirements.txt
python app.py          # 终端1：启动靶场
pytest -v              # 终端2：运行测试