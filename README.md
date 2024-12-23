Documentación del Script para Eliminar Fondo de Imágenes con API
Descripción:
Este script utiliza la API de remove.bg para eliminar el fondo de una imagen. La imagen original debe estar disponible localmente, y el resultado se guarda en un archivo de salida.

Requisitos:
Python instalado en el sistema (versión compatible).

Biblioteca requests instalada. Puedes instalarla con:

bash
Copy code
pip install requests
Tener una clave API válida de remove.bg.

Instrucciones de Uso:
Guarda la imagen en la misma carpeta donde está el script, con el nombre especificado en input_path (por defecto, hiramcito.jpg).
Reemplaza el valor de api_key con tu propia clave de la API.
Ejecuta el script usando:
bash
Copy code
python nombre_del_script.py
Notas Importantes:
La API de remove.bg tiene un límite de uso según el plan que tengas. Revisa las políticas de uso antes de realizar muchas solicitudes.
El archivo resultante se guarda como hiramcito.png en la misma ubicación que el script.
Ejemplo de Respuesta Exitosa:
Si la API procesa correctamente la imagen, verás el siguiente mensaje en la consola:

bash
Copy code
Fondo eliminado. Imagen guardada en hiramcito.png
Posibles Errores y Soluciones:
403 - API Key invalid: La clave de la API no es válida. Asegúrate de que sea correcta y esté activa.
404 - File not found: El archivo de entrada no existe. Revisa la ruta especificada en input_path.
Otros errores pueden estar relacionados con el límite de uso de la API o problemas de conexión.
