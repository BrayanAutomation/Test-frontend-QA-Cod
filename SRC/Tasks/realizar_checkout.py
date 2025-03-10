from SRC.UserInterfaces.checkout_ui import CheckoutUI
from SRC.Interactions.hacer_click import HacerClick
from SRC.Interactions.escribir import Escribir
from playwright.sync_api import Page

def realizar_checkout(page: Page, nombre: str, apellido: str, codigo_postal: str):
    Escribir.en(page, CheckoutUI.NOMBRE, nombre)
    Escribir.en(page, CheckoutUI.APELLIDO, apellido)
    Escribir.en(page, CheckoutUI.CODIGO_POSTAL, codigo_postal)
    HacerClick.en(page, CheckoutUI.CONTINUAR)
    HacerClick.en(page, CheckoutUI.FINALIZAR)