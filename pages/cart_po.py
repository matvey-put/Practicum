from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.firstName = page.locator("[data-test=\"firstName\"]")
        self.lastName = page.locator("[data-test=\"lastName\"]")
        self.postalCode = page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")
        self.finish_button = page.locator("[data-test=\"finish\"]")
        self.complete_header = page.locator("[data-test=\"complete-header\"]")
        

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def make_order(self, firstName, lastName, postalCode):
        self.firstName.fill(firstName)
        self.lastName.fill(lastName)
        self.postalCode.fill(postalCode)
        self.continue_button.click()
        self.finish_button.click()
        