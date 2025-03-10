# Test-frontend-QA-Cod
## Automatización de Pruebas **Saucedemo** con Playwright, Behave y Screenplay

Este proyecto es una automatización de pruebas para el sitio web **SauceDemo**, utilizando **Playwright** como herramienta de automatización, **Behave** para la definición de escenarios en lenguaje Gherkin y el patrón **Screenplay** para estructurar el código de manera modular y mantenible.

---

## Tabla de Contenidos
1. [Requisitos](#requisitos)
2. [Instalación](#instalación)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Ejecución de Pruebas](#ejecución-de-pruebas)
5. [Patrón Screenplay](#patrón-screenplay)

---

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.11** o superior.
- **Playwright**: Herramienta de automatización de navegadores.
- **Behave**: Framework para pruebas BDD (Behavior-Driven Development).
- **Git**: Para clonar el repositorio.

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/BrayanAutomation/Test-frontend-QA-Cod.git

   Usa este comando en la ruta de tu equipo, donde quieras clonar el pryecto.

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

4. Instala los navegadores necesarios para Playwright:
   ```bash
   playwright install

---


## Patrón Screenplay

El proyecto utiliza el patrón Screenplay, que es un enfoque de diseño para automatización de pruebas que promueve la reutilización de código y la claridad. Aquí está cómo se estructura:

- **UserInterface:** Contiene los selectores y métodos para interactuar con las páginas web.
- **Tasks:** Representan acciones que un usuario puede realizar (por ejemplo, iniciar sesión, agregar productos al carrito).
- **Questions:** Validaciones y preguntas sobre el estado de la aplicación (por ejemplo, verificar si un mensaje está visible).
- **Interactions:** Interacciones básicas como clics, escritura, etc.

---

## Ejecución de Pruebas

Para ejecutar las pruebas, sigue estos pasos:

1. Asegúrate de estar en el directorio raíz del proyecto.

2. Ejecuta el siguiente comando:
   ```bash
   behave TEST
---

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

- **Nombre:** Brayan Granado
- **Email:** brayan.sus7@gmail.com
- **GitHub:** BrayanAutomation


## Estructura del Proyecto

 El proyecto está organizado de la siguiente manera:   
   ```bash
   saucedemo-automation/
   ├── SRC/
   │   ├── UserInterface/                   # Locators, Web Elements
   │   ├── interactions/                    # Interacciones básicas (clics, escritura, etc.)
   │   ├── Task/                            # Tareas del patrón Screenplay
   │   └── Questions/                       # Validaciones y preguntas sobre el estado de la aplicación
   ├── TEST/
   │   ├── Features/                        # Archivos .feature con los escenarios en Gherkin
   │   └── steps/                           # Implementación de los pasos de los escenarios
   ├── behave.ini                           # Configuración de Behave
   ├── environment.py                       # Configuración del entorno de pruebas
   └── requirements.txt                     # Dependencias del proyecto   
