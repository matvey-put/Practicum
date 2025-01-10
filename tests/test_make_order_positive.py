from playwright.sync_api import Page, expect
from pages.login_po import LoginPage
from pages.products_po import ProductsPage
from pages.cart_po import CartPage

def test_make_order_positive(page: Page):
    lp = LoginPage(page)
    lp.navigate()
    lp.login("standard_user", "secret_sauce")

    pp = ProductsPage(page)
    pp.click_add_to_cart_bike()
    pp.click_cart()

    cp = CartPage(page)
    cp.make_order('a', 'b', '1')

    expect(cp.complete_header).to_have_text("Thank you for your order!")