from playwright.sync_api import Page

def verificar_mensaje(page: Page, mensaje: str):
    return page.inner_text(".complete-header") == mensaje