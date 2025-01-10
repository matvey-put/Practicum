from playwright.sync_api import Page, expect
from pages.login_po import LoginPage

def test_login_uncorrect(page: Page) -> None:
    lp = LoginPage(page)
    lp.navigate()
    lp.login("standard_user", "wrong_password")
    expect(lp.error).to_contain_text("Epic sadface: Username and password do not match any user in this service")