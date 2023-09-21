from selene.support.shared import browser


def test_open_google():
    browser.open('https://google.com')
    browser.config.driver.fullscreen_window()