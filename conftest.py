import pytest
from playwright.sync_api import sync_playwright
from pages.resume_page import ResumePage

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def resume_page(page):
    return ResumePage(page)