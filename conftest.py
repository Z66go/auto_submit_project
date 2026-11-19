import pytest

def pytest_configure(config):
    """ 全局配置，在 pytest 运行测试前自动执行 """
    # 告诉所有 pytest 测试用例，浏览器默认使用无头模式运行
    config.addinivalue_line(
        "markers", "slow: mark test as slow to run"
    )
    print("已启用无头模式，准备在后台静默运行测试...")

# 强制让 pytest-playwright 插件在无头模式下运行
# 这行代码会确保你在 resume_page 里调用的浏览器是后台运行的
def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=True,
        help="Run in headless mode",
    )