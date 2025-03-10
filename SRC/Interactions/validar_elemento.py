from playwright.sync_api import Page

class ValidarElemento:
    @staticmethod
    def este_visible(page: Page, webElement: str):
        assert page.locator(webElement).is_visible(), f"Error: El elemento '{webElement}' no está visible en la pantalla."
