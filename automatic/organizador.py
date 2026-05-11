from pathlib import Path
import os 

carpeta_objetivo = Path.home() / "des"

#se crea diccionario 

categorias = {

        "Imagenes" : [".png", ".jpg", ".gif"],

        "Documento" : [".pdf", ".docx", ".txt", ".xlsx"],

        "Videos" : [".mp4", ".avi", ".mkv"],

        "Musica" : [".mp3", ".wav"],

}

categorias_predeterminadas =["Otros"] 

extension_a_categoria = {}
for categoria, exts in categorias.items():
    for ext in exts:
        extension_a_categoria[ext.lower()] = categoria



#listar archivos y filtrar

archivos= [f for f in carpeta_objetivo.iterdir() if f.is_file()]#itedir() lista contenidos

for archivo in archivos:
    ext = archivo.suffix.lower()#archivo.suffix da la extensión (con punto).
    categoria = extension_a_categoria. get(ext,"Otros")
    destino_dir=carpeta_objetivo / categoria
    destino_dir.mkdir(exist_ok=True)
    archivo.rename(destino_dir / archivo.name)
    print(f"Movido {archivo.name} a {categoria}/")