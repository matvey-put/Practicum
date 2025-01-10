from playwright.sync_api import expect

from pages.login_po import LoginPage
from pages.products_po import ProductsPage

def test_product_sort(page):
    lp = LoginPage(page)
    pp= ProductsPage(page)

    lp.navigate()
    lp.login("standard_user", "secret_sauce")

    pp.select_sort_lohi()

    expect(pp.inventory_item_price).to_have_text(['$7.99', '$9.99', '$15.99', '$15.99', '$29.99', '$49.99'])