import sys
import MySQLdb
def conectar_bbdd(host,usuario,password,nombrebd):
    try:
        db = MySQLdb.connect(host,usuario,password,nombrebd)
        return db
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)

def MostrarMenu():
    menu='''
    1. Listar Equipos
    2. Buscar Equipo
    3. Informacion Relacionada Equipo
    4. Eliminar Equipo
    5. Añadir Equipo
    6. Actualizar Entrenador
    0. Salir
    '''
    print(menu)
    while True:
        try:
            opcion=int(input("Opción:"))
            return opcion
        except:
            print("Opción incorrecta, debe ser un número")

def listar_equipo(db,comunidad):
    sql="select posicion,nombre from liga where nombre in(select nombre from equipos where comunidad='%s') order by posicion ASC;" % comunidad
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
       cursor.execute(sql)
       registros = cursor.fetchall()
       for registro in registros:
          print(registro["posicion"]," --- ",registro["nombre"])
    except:
       print("Error en la consulta")

def Buscar_equipo(db,equipo):
    sql="select estadio,nombre_entrenador,nombre_presidente,anyo_fundacion from equipos where nombre='%s';" % equipo
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        if cursor.rowcount==0:
            print("No hay equipos con ese nombre.")
        else:
            registros = cursor.fetchall()
            for registro in registros:
                print("Estadio:",registro["estadio"],"--","Entrenador:",registro["nombre_entrenador"],"--","Presidente:",registro["nombre_presidente"],"--","Año Fundacion:",registro["anyo_fundacion"])
    except:
       print("Error en la consulta")

def champs_league(db,equipo):
    sql="select nombre from equipos where nombre in (select nombre from liga where posicion<='4');"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            if equipo == registro["nombre"]:
                print(equipo,"va a la UEFA CHAMPIONS LEAGUE")
    except:
        print("Error")

def eur_league(db,equipo):
    sql="select nombre from equipos where nombre in (select nombre from liga where posicion>'4' and posicion<='7');"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            if equipo == registro["nombre"]:
                print(equipo,"va a la UEFA EUROPA LEAGUE")
    except:
        print("Error")

def no_compt(db,equipo):
    sql="select nombre from equipos where nombre in (select nombre from liga where posicion>'7' and posicion<='17');"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)     
        registros = cursor.fetchall()
        for registro in registros:
            if equipo == registro["nombre"]:
                print(equipo,"no va a competicion europea")
    except:
        print("Error")

def desc_liga(db,equipo):
    sql="select nombre from equipos where nombre in (select nombre from liga where posicion>'17' and posicion<='20');"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            if equipo == registro["nombre"]:
                print(equipo,"desciende a segunda division")
    except:
        print("Error")

def eliminar_equipo(db,equipo):
    sql="delete from liga where nombre='%s';" % equipo
    sql1="delete from equipos where nombre='%s'" % equipo
    cursor = db.cursor()
    resp=input("¿Realmente quieres borrar el equipo introducido? (pulsa 's' para si)")
    if resp=="s":
        try:
            cursor.execute(sql)
            db.commit()
            cursor.execute(sql1)
            db.commit()
        except:
            ("ERROR AL BORRAR")

def anadir_ascendidos(db,equipo,liga):
    cursor = db.cursor()
    sql="INSERT INTO equipos VALUES('%s','%s',null,'%d','%s','%s','%s','%s');" % (equipo["nombre"],equipo["estadio"],equipo["n_jugadores"],equipo["nombre_entrenador"],equipo["nombre_presidente"],equipo["anyo_fundacion"],equipo["comunidad"])
    sql1="INSERT INTO liga VALUES('%s','%s','0','0','0','0','0')" % (liga["posicion"],equipo["nombre"])
    try:
        cursor.execute(sql)
        db.commit()
        cursor.execute(sql1)
        db.commit()
    except:
        print("Error al insertar.")
        db.rollback()

def actualizar_entrenador(db,entrenador,equipo):
    cursor = db.cursor()
    sql="update equipos set nombre_entrenador='%s' where nombre='%s'" % (entrenador["nombre_entrenador"],equipo["nombre"])
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al actualizar")

def Desconectar_BBDD(db):
    db.close()