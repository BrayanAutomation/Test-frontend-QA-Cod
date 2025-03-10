Feature: Compra de productos en SauceDemo

  Scenario: Usuario compra productos exitosamente
    Given el usuario abre la página de inicio de sesión
    When inicia sesión con usuario "standard_user" y contraseña "secret_sauce" visualizando el inventario de productos
    And agrega los productos "Test.allTheThings() T-Shirt (Red)" y "Sauce Labs Bike Light" al carrito
    And accede al carrito y verifica los productos agregados
    And procede al checkout ingresando "Brayan", "Perez" y "110011"
    Then debe ver el mensaje de confirmación de compra "Thank you for your order!"