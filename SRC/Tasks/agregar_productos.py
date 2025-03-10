from SRC.UserInterfaces.inventario_ui import InventarioUI
from SRC.Interactions.hacer_click import HacerClick
from playwright.sync_api import Page

def agregar_productos(page: Page, producto1: str, producto2: str):
    HacerClick.en(page, InventarioUI.PRODUCTO_1)
    HacerClick.en(page, InventarioUI.PRODUCTO_2)