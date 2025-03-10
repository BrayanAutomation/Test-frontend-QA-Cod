from playwright.sync_api import Page

class Escribir:
    @staticmethod
    def en(page: Page, selector: str, texto: str):
        page.fill(selector, texto)