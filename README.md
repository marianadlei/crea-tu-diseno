# Crea tu Diseño

Este proyecto permite a los usuarios personalizar productos y visualizar sus diseños en tiempo real, integrándose con Shopify para facilitar la cotización y el proceso de compra.

## 🚀 Funcionalidades

- Generación de diseños personalizados mediante un formulario interactivo.
- Visualización en tiempo real basada en los parámetros seleccionados.
- Integración con Shopify para gestionar cotizaciones y pedidos.
- Soporte para materiales sostenibles como el bambú.

## 🔧 Tecnologías utilizadas

- **Backend**: Python con Flask.
- **Frontend**: Shopify para la interfaz de usuario y personalización.
- **API**: Integración con OpenAI para generación visual.
- **Otros**: Archivos `.env` para manejar configuraciones sensibles.

## 🗂️ Estructura del proyecto

```
CreaTuDiseño/
├── Server/
│   ├── app.py               # Código principal del servidor Flask
│   ├── requirements.txt     # Dependencias del proyecto
│   ├── test_flask.py        # Pruebas para verificar el servidor
│   ├── .gitignore           # Archivos ignorados por Git
```

## 🔧 Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/marianadlei/crea-tu-diseno.git
   cd crea-tu-diseno/Server
   ```

2. **Instalar dependencias**:
   Asegúrate de tener Python instalado. Luego, ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**:
   Crea un archivo `.env` en la carpeta `Server` con el siguiente contenido:
   ```
   OPENAI_API_KEY=tu_api_key_aqui
   ```

4. **Iniciar el servidor**:
   Ejecuta el servidor Flask:
   ```bash
   python app.py
   ```

5. **Probar el servidor**:
   Ve a `http://127.0.0.1:5000` en tu navegador para verificar que el servidor esté funcionando.

## 🌐 Integración con Shopify

El proyecto está diseñado para integrarse con Shopify como una sección personalizada donde los usuarios pueden acceder al formulario de diseño interactivo.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas colaborar, envía un **Pull Request** con tus sugerencias.
