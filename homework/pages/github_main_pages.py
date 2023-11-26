from selene import browser, have


class MainPage:
    def open(self):
        browser.open('https://github.com/')
        return self

    def click_login_button_desktop(self):
        browser.element('.HeaderMenu-link--sign-in').click()
        return self

    def click_login_button_mobile(self):
        browser.element('.Button--link').click()
        browser.element('.HeaderMenu-link--sign-in').click()
        return self

    def redirect_to_login_page(self):
        browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
        return self
