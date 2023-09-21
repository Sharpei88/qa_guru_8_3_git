from selene.support.shared import browser


def test():
    browser.open('https://google.com')
    browser.config.driver.fullscreen_window()