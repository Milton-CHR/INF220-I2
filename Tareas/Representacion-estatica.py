# Representacion estatica
libros={} 
def agregar_libro(titulo, autor, isbn, genero):
    libros[isbn]={
        "titulo":titulo,
        "autor":autor,
        "genero":genero
    }

def buscar_libro(dato):
    resultados=[]
    for codigo, info in libros.items():
        if dato in info["titulo"] or dato in info["autor"] or dato==codigo:
            resultados.append(info)
    if resultados==[]:
        print("no encontre nada")
    return resultados

def mostrar_libros():
    if len(libros)==0:
        print("no hay libros guardados")
    else:
        for codigo, info in libros.items():
            print("isbn:", codigo, "titulo:", info["titulo"], "autor:", info["autor"], "genero:", info["genero"])

# prueba
agregar_libro("Cien años de soledad", "Garcia Marquez", "72345", "novela")
agregar_libro("El principito", "Antoine", "72534", "infantil")

print("TODOS LOS LIBROS:")
mostrar_libros()

print("BUSQUEDA:")
print(buscar_libro("Marquez"))
