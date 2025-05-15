from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple, List

class BasePage:
    """Base class for all page objects providing common web interaction methods."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the base page object.

        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        """
        Find a single element on the page with explicit wait.

        Args:
            locator: Tuple of By strategy and locator string

        Returns:
            WebElement: Found element
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: Tuple[str, str]) -> List[WebElement]:
        """
        Find multiple elements on the page with explicit wait.

        Args:
            locator: Tuple of By strategy and locator string

        Returns:
            List[WebElement]: List of found elements
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator: Tuple[str, str]) -> None:
        """
        Click on an element.

        Args:
            locator: Tuple of By strategy and locator string
        """
        self.find_element(locator).click()

    def send_keys(self, locator: Tuple[str, str], text: str) -> None:
        """
        Send text to an element.

        Args:
            locator: Tuple of By strategy and locator string
            text: Text to send to the element
        """
        self.find_element(locator).send_keys(text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        """
        Get text from an element.

        Args:
            locator: Tuple of By strategy and locator string

        Returns:
            str: Text content of the element
        """
        return self.find_element(locator).text
