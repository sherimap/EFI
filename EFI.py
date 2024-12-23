import requests

# Configuración de la API y rutas de archivo
input_path = 'hiramcito.jpg'
output_path = 'hiramcito.png'
api_key = '7NfqCXM4m6tfTNKXcLuUkoYG'  # Reemplázala por tu clave de remove.bg

# Leer la imagen y enviar la solicitud
with open(input_path, 'rb') as file:
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': file},
        data={'size': 'auto'},
        headers={'X-Api-Key': api_key},
    )

# Manejar la respuesta
if response.status_code == 200:
    with open(output_path, 'wb') as out_file:
        out_file.write(response.content)
    print(f"Fondo eliminado. Imagen guardada en {output_path}")
else:
    print(f"Error: {response.status_code} - {response.text}")