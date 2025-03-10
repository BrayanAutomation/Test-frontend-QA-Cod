from SRC.UserInterfaces.inventario_ui import InventarioUI
from SRC.UserInterfaces.checkout_ui import CheckoutUI
from SRC.Interactions.hacer_click import HacerClick
from SRC.Interactions.validar_elemento import ValidarElemento
from playwright.sync_api import Page

def acceder_al_carrito(page: Page):
    HacerClick.en(page, InventarioUI.CARRITO)
    ValidarElemento.este_visible(page, InventarioUI.VALIDAR_TSHIRT)
    ValidarElemento.este_visible(page, InventarioUI.VALIDAR_BIKE)
    HacerClick.en(page, CheckoutUI.BOTON_CHECKOUT)