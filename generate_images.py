import os

# Obtener la ruta absoluta del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta completa de la carpeta 'Images' que está en el mismo directorio del script
folder = os.path.join(script_dir, 'Images')

# Mostrar la ruta completa
print(f"📁 Carpeta a escanear: {folder}")

# Verifica que la carpeta exista
if not os.path.isdir(folder):
    print(f"⚠️ La carpeta 'Images' no existe en el directorio del script.")
else:
    # Extensiones válidas
    extensiones = ('.jpg', '.jpeg', '.png', '.gif', '.webp')

    # Obtener lista de imágenes ordenadas
    images = sorted([f for f in os.listdir(folder) if f.lower().endswith(extensiones)])

    # Generar array de JavaScript con rutas relativas
    js_array = "const images = [\n    '" + "',\n    '".join(f"Images/{img}" for img in images) + "'\n];"

    # Imprimir resultado
    print("\n📜 Copia esto dentro de la sección <script> de tu index.html:")
    print(js_array)
