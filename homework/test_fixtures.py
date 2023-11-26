"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have
from homework.pages.github_main_pages import MainPage

@pytest.fixture
def desktop_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()


@pytest.fixture
def mobile_setup():
    browser.config.window_width = 414
    browser.config.window_height = 896

    yield

    browser.quit()


def test_github_desktop(desktop_setup):
    main_page = MainPage()
    main_page.open()
    main_page.click_login_button_desktop()
    main_page.redirect_to_login_page()


def test_github_mobile(mobile_setup):
    main_page = MainPage()
    main_page.open()
    main_page.click_login_button_mobile()
    main_page.redirect_to_login_page()
