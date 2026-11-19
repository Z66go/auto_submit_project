import pytest
# tests/test_submit.py


def test_submit_single_person(resume_page):
    """正常提交单人简历"""
    resume_page.goto()
    resume_page.fill_form(
        username="张三",
        email="zhangsan@example.com",
        file_path="test_submit.txt",
    )
    resume_page.click_submit()
    assert "张三 提交成功！" in resume_page.get_result_text(), "正常提交失败"


def test_submit_without_name(resume_page):
    """姓名留空提交"""
    resume_page.goto()
    resume_page.fill_form(
        username="",
        email="test@example.com",
        file_path="test_submit.txt",
    )
    resume_page.click_submit()
    assert "请填写姓名" in resume_page.get_result_text(), "空姓名未提示校验"