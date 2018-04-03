
from Globales import *

def actualizarDiccionarioModificado(id, opcion , valor):
     for i in biblioteca:
         if (i["id"]== id):
             if(opcion == "1"):
                 i["nombreAutor"] = valor
             elif(opcion == "2"):
                 i["tituloObra"] = valor
             elif(opcion == "3"):
                 i["anno"] = valor
     return False


def buscarLibro(id):
    global  biblioteca

    for i in biblioteca:
        if(i["id"]== id):
            return i
    return False



def crearLibro(pnombreA, ptitulo, pid , panno):

    global biblioteca

    libro = {}
    libro["nombreAutor"] = pnombreA
    libro["tituloObra"] = ptitulo
    libro["id"]= pid
    libro["anno"]= panno
    biblioteca.append(libro)


def eliminarLibro(pid):

    global biblioteca
    for i in biblioteca:
        if(i["id"]== pid):
            biblioteca.remove(i)
            return True #libro eliminado

    return False #Libro no encontrado