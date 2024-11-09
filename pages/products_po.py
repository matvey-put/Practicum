from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_container=page.locator("[data-test=\"inventory-container\"]")
        self.inventory_list= page.locator("[data-test=\"inventory-list\"]")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/inventory.html>")
