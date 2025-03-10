class InventarioUI:
    INVENTARIO = "//div[@class='app_logo']"
    PRODUCTO_1 = '#add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)'
    PRODUCTO_2 = '#add-to-cart-sauce-labs-bike-light'
    VALIDAR_TSHIRT = "//div[@class='inventory_item_name' and contains(text(), 'T-Shirt')]"
    VALIDAR_BIKE = "//div[@class='inventory_item_name' and contains(text(), 'Sauce Labs Bike Light')]"
    CARRITO = '#shopping_cart_container'