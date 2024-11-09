from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_container=page.locator("[data-test=\"inventory-container\"]")
        self.inventory_list= page.locator("[data-test=\"inventory-list\"]")
        self.add_bike_light=page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        self.shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")
        self.checkout = page.locator("[data-test=\"checkout\"]")

    def click_add_to_cart_bike(self):
        self.add_bike_light.click()

    def click_cart(self):
        self.shopping_cart_link.click()
        self.checkout.click()

        

    
    
