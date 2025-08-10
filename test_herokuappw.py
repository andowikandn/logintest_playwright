from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture

def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://the-internet.herokuapp.com/login')
        yield page
        browser.close()

input_credentialsX = [('',''),
                     ('tomsmith',''),
                     ('','SuperSecretPassword!'),
                     ('typo','typo')
                    ]

input_credentialsY = [('tomsmith','SuperSecretPassword!')]


@pytest.mark.negativetest
@pytest.mark.parametrize('a,b', input_credentialsX)
def test_login_error(a,b,page):
    page.fill('input#username', a)
    page.fill('input#password', b)
    page.get_by_role('button', name='Login').click()
    alert = page.locator('.flash.error')
    page.screenshot(path='error_message.png')
    assert alert.is_visible()
    page.click('a.close')


@pytest.mark.positivetest
@pytest.mark.parametrize('c,d', input_credentialsY)
def test_login_success(c,d,page):
    page.fill('input#username', c)
    page.fill('input#password', d)
    page.get_by_role('button', name='Login').click()
    alert = page.locator('.flash.success')
    page.screenshot(path='login_success.png')
    assert alert.is_visible()
    page.click('a.close')


@pytest.mark.positivetest
@pytest.mark.parametrize('c,d', input_credentialsY)
def test_logout(c,d,page):
    test_login_success(c,d,page)
    page.locator('a[href="/logout"]').click()
    alert = page.locator('.flash.success')
    page.screenshot(path='logout_success.png')
    assert alert.is_visible()
    page.click('a.close')