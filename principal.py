from funciones import *
db = conectar_bbdd("localhost","joseju","pass123","proyecto")
opcion=MostrarMenu()
while opcion!=0:
    if opcion==1:
        comunidad1=input("Introduzca la comunidad:")
        listar_equipo(db,comunidad1)
    elif opcion==2:
        equipo1=input("Equipo:")
        Buscar_equipo(db,equipo1)
    elif opcion==3:
        equipo2=input("Equipo:")
        if equipo2 == champs_league(db,equipo2):
            champs_league(db,equipo2)
        elif equipo2 == eur_league(db,equipo2):
            eur_league(db,equipo2)
        elif equipo2 == no_compt(db,equipo2):
            no_compt(db,equipo2)
        elif equipo2 == desc_liga(db,equipo2):
            desc_liga(db,equipo2)
    elif opcion==4:
        equipo5=input("Introduzca el equipo que quiera eliminar:")
        eliminar_equipo(db,equipo5)
    elif opcion==5:
        equipo3={}
        liga1={}
        equipo3["nombre"]=input("Equipo:")
        equipo3["estadio"]=input("Estadio:")
        equipo3["n_jugadores"]=int(input("Numero jugadores:"))
        equipo3["nombre_entrenador"]=input("Nombre Entrenador:")
        equipo3["nombre_presidente"]=input("Nombre Presidente:")
        equipo3["anyo_fundacion"]=input("Año Fundacion:")
        equipo3["comunidad"]=input("Comunidad del equipo:")
        liga1["posicion"]=input("Posicion liga:")
        anadir_ascendidos(db,equipo3,liga1)
    elif opcion==6:
        entrenador1={}
        equipo4={}
        entrenador1["nombre_entrenador"]=input("Introduzca el nombre del entrenador:")
        equipo4["nombre"]=input("Introduzca el nombre del equipo:")
        actualizar_entrenador(db,entrenador1,equipo4)
    opcion=MostrarMenu()
Desconectar_BBDD(db)