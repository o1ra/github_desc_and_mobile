"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080, 'desktop'), (393, 852, 'mobile')])
def browser_setup(request):
    browser.config.base_url = 'https://github.com/'
    if request.param[2] == 'desktop':
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return request.param[2]

    if request.param[2] == 'mobile':
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return request.param[2]


def test_github_desktop(browser_setup):
    if browser_setup == 'mobile':
        pytest.skip('this test for desktop browsers')
    browser.open('')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_github_mobile(browser_setup):
    if browser_setup == 'desktop':
        pytest.skip('this test for mobile browsers')
    browser.open('')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))