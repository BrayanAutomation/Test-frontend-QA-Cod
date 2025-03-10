from playwright.sync_api import Page

class HacerClick:
    @staticmethod
    def en(page: Page, selector: str):
        page.click(selector)