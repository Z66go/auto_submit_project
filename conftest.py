import pytest

# --- 你之前的强制无头模式代码（完美保留） ---
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "slow: mark test as slow to run"
    )
    print("\n已启用无头模式，准备在后台静默运行测试...")

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=True,
        help="Run in headless mode",
    )

# --- 补全的缺失代码（CI 正在等它） ---
@pytest.fixture
def resume_page(page):
    """
    核心修复：定义 resume_page fixture
    它负责将 playwright 启动好的 page 实例，
    初始化为你在 tests 里用到的 ResumePage 对象
    """
    from pages.resume_page import ResumePage
    return ResumePage(page)