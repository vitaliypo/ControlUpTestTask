from typing import Optional

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Represents the inventory page in the application."""

    # Locators
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".inventory_item:first-child button")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_inventory_items_count(self) -> int:
        return len(self.find_elements(self.INVENTORY_ITEMS))

    def add_first_item_to_cart(self) -> None:
        self.click(self.ADD_TO_CART_BUTTON)

    def get_cart_badge_count(self) -> Optional[int]:
        try:
            return int(self.get_text(self.CART_BADGE))
        except NoSuchElementException:
            return None
        except ValueError as e:
            # If this happens, it means the badge is present but contains invalid data
            raise ValueError(f"Cart badge contains invalid number: {e}")
