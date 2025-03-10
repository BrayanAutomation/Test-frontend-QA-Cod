from SRC.UserInterfaces.login_ui import LoginUI
from SRC.UserInterfaces.inventario_ui import InventarioUI
from SRC.Interactions.hacer_click import HacerClick
from SRC.Interactions.escribir import Escribir
from SRC.Interactions.validar_elemento import ValidarElemento
from playwright.sync_api import Page

def iniciar_sesion(page: Page, usuario: str, contrasena: str):
    Escribir.en(page, LoginUI.USUARIO, usuario)
    Escribir.en(page, LoginUI.CONTRASENA, contrasena)
    HacerClick.en(page, LoginUI.BOTON_LOGIN)
    ValidarElemento.este_visible(page, InventarioUI.INVENTARIO)