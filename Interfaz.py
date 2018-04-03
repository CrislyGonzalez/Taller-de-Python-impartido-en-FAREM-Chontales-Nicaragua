# importando archivo o librerías
from logica import *

def imprimirLibro(libro):

    print("\n Imprimiendo libro...\n"
          "\nNombre del Libro: " , libro["tituloObra"],"\n"
          "\nAutor: ", libro["nombreAutor"],"\n"
          "\nAño de publicación: ", libro["anno"],"\n")

def verLibros():

    for i in biblioteca:
        print("\n Nombre del Libro: ", i["tituloObra"],"\n"
        " Nombre del autor: ", i["nombreAutor"], "\n"
        "Año de publicación: ", i["anno"],"\n")

def menuModificar(id):

    opcion = input("\n **Menu modificar elementos de un libro **\n"
                   "1. Autor\n"
                   "2. Nombre del libro\n"
                   "3. Año de creación\n"
                   "4. Regresar a menu principal\n"
                   " Opción: ")

    if(opcion == "1"):
        valor = input("Ingrese el nuevo nombre del autor\n")
        request = actualizarDiccionarioModificado(id,opcion, valor)

        if  not request: # request == False
            print("\nLibro actualizado\n")
            menuModificar(id)
        else:
            print("\n Libro no encontrado")

    elif(opcion == "2"):
        valor = input("Ingrese el nuevo nombre del libro\n")
        actualizarDiccionarioModificado(id,opcion, valor)
        print("\nLibro actualizado\n")
        menuModificar(id)

    elif(opcion == "3"):
        valor = input("Ingrese el nuevo año de creación del libro\n")
        actualizarDiccionarioModificado(id,opcion, valor)
        print("\nLibro actualizado\n")
        menuModificar(id)

    elif(opcion == "4"):
        main()




def ingresarLibro():

    autor = input("Ingrese el nombre del autor del libro: ")
    nombreLibro = input("Ingrese el nombre del libro: ")
    id = input("Ingrese el codigo del libro: ")
    anno = input("Ingrese el año de publicación del libro: ")
    crearLibro(autor,nombreLibro,id,anno)

def main():

    opcion= int(input("**Menu principal**"
                      "Bienvenido al sistema de librería\n"
                      "1. Ingresar un libro\n"
                      "2. Modificar un libro\n"
                      "3. Eliminar un libro\n"
                      "4. Buscar un libro\n"
                      "5. Ver todos los libros\n"
                      "6. Salir\n"
                      " Opción: "))
    if opcion == 1:
        ingresarLibro()
        main()

    elif opcion == 2:
        id = input("Ingrese el código que desea modificar")
        menuModificar(id)

    elif opcion == 3:
        idEliminar = input("Ingrese el código que desea eliminar: ")
        request = eliminarLibro(idEliminar)
        if(request == True):
            print("\nLibro eliminado\n")
            main()

    elif opcion == 4:
        id = input("Ingrese el código del libro que desea buscar: ")
        request = buscarLibro(id)
        if(request != False):
            imprimirLibro(request)
            main()
        else:
            print("\nLibro no encontrado\n")
            main()

    elif opcion == 5:
        verLibros()
        main()


    elif opcion == 6:
        return


main()
