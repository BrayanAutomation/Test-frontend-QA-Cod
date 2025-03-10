from behave import given, when, then
from SRC.Tasks.iniciar_sesion import iniciar_sesion
from SRC.Tasks.agregar_productos import agregar_productos
from SRC.Tasks.acceder_al_carrito import acceder_al_carrito
from SRC.Tasks.realizar_checkout import realizar_checkout
from SRC.Questions.verificar_mensaje import verificar_mensaje

@given("el usuario abre la página de inicio de sesión")
def abrir_pagina(context):
    context.page.goto("https://www.saucedemo.com/")

@when("inicia sesión con usuario \"{usuario}\" y contraseña \"{contrasena}\" visualizando el inventario de productos")
def iniciar_sesion_step(context, usuario, contrasena):
    iniciar_sesion(context.page, usuario, contrasena)  

@when("agrega los productos \"{producto1}\" y \"{producto2}\" al carrito")
def agregar_productos_step(context, producto1, producto2):
    agregar_productos(context.page, producto1, producto2)  

@when("accede al carrito y verifica los productos agregados")
def verificar_carrito(context):
    acceder_al_carrito(context.page) 

@when("procede al checkout ingresando \"{nombre}\", \"{apellido}\" y \"{codigo_postal}\"")
def realizar_checkout_step(context, nombre, apellido, codigo_postal):
    realizar_checkout(context.page, nombre, apellido, codigo_postal)  

@then("debe ver el mensaje de confirmación de compra \"{mensaje}\"")
def verificar_confirmacion(context, mensaje):
    assert verificar_mensaje(context.page, mensaje), "El mensaje de confirmación no es correcto" 
