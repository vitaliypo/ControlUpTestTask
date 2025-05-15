import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.inventory_page import InventoryPage
from config.test_configuration import TestConfig
from pages.login_page import LoginPage


class TestBase:
    """Base class for Sauce Demo tests with common setup and helper methods."""

    @pytest.fixture(autouse=True)
    def setup_browser(self):
        """Setup Chrome browser with common configuration."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def setup_pages(self):
        """Initialize page objects and navigate to base URL."""
        self.driver.get(TestConfig.SAUCE_DEMO_URL)
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)

    def perform_standard_login(self):
        """Helper method to perform login with standard user credentials."""
        self.login_page.login(
            username=TestConfig.STANDARD_USERNAME,
            password=TestConfig.STANDARD_PASSWORD
        )


class TestInventoryFeatures(TestBase):
    """Test cases for Sauce Demo inventory functionality."""

    def test_should_display_correct_number_of_inventory_items(self):
        """Verify that inventory page shows the expected number of items."""
        self.perform_standard_login()
        actual_count = self.inventory_page.get_inventory_items_count()
        assert actual_count == 6

    def test_should_update_cart_badge_when_adding_item(self):
        """Verify that cart badge updates after adding an item to cart."""
        self.perform_standard_login()
        self.inventory_page.add_first_item_to_cart()
        assert self.inventory_page.get_cart_badge_count() == 1
