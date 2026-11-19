content = '''from playwright.sync_api import Page


class ResumePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("http://localhost:5000")

    def fill_name(self, name: str):
        self.page.fill("#username", name)

    def fill_email(self, email: str):
        self.page.fill("#email", email)

    def upload_resume(self, file_path: str):
        self.page.set_input_files("#resume", file_path)

    def click_submit(self):
        self.page.click("#submit-btn")

    def get_result_text(self) -> str:
        self.page.wait_for_selector("#result", state="visible")
        return self.page.text_content("#result")

    def fill_form(self, username: str, email: str, file_path: str = None):
        self.fill_name(username)
        self.fill_email(email)
        if file_path:
            self.upload_resume(file_path)
'''

with open('pages/resume_page.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("写入成功")