-- CREAMOS LA BASE DE DATOS
CREATE DATABASE proyecto;
-- CREAMOS EL USUARIO PARA LA BASE DE DATOS
CREATE USER 'joseju'@'localhost' IDENTIFIED BY 'pass123';
GRANT ALL PRIVILEGES ON proyecto.* TO 'joseju'@'localhost';
exit
-- CREACION TABLAS-------------------------------------------------------------------------
create table equipos(
    nombre varchar(20) unique,
    estadio varchar(20),
    fecha_debut date,
    n_jugadores int(2),
    nombre_entrenador varchar(20) unique,
    nombre_presidente varchar(20) unique,
    anyo_fundacion varchar(4),
    comunidad varchar(20),
    constraint pk_equipos primary key(nombre)
);

create table liga(
    posicion int(3) unique,
    nombre varchar(20) unique,
    p_ganados int(2),
    p_perdidos int(2),
    p_empatados int(2),
    g_favor int(3),
    g_contra int(3),
    constraint pk_liga primary key(posicion,nombre),
    constraint fk_equipos foreign key(nombre) references equipos(nombre)
);

----INSERTS------------------------------------------------------------------------------------------------------------
----EQUIPOS------------------------------------------------------------------------------------------------------------
INSERT INTO equipos VALUES('Real Madrid','Santiago Bernabeu','2019/08/15','26','Zinedine Zidane','Florentino Perez','1902','Madrid');
INSERT INTO equipos VALUES('FC Barcelona','Camp Nou','2019/08/15','27','Xavi Hernandez','Joan Laporta','1899','Cataluña');
INSERT INTO equipos VALUES('Atletico de Madrid','Wanda Metropolitano','2019/08/15','26','Cholo Simeone','Enrique Cerezo','1903','Madrid');
INSERT INTO equipos VALUES('Sevilla FC','Sanchez Pizjuan','2019/08/15','26','Julen Lopetegui','Jose Castro','1885','Andalucia');
INSERT INTO equipos VALUES('Villareal CF','Estadio la Ceramica','2019/08/15','26','Unai Emery','Miguel Diaz','1934','Comunidad Valenciana');
INSERT INTO equipos VALUES('Real Sociedad','Erreale Arena','2019/08/15','26','Imanol Alguacil','Ibai LLanos','1921','Pais Vasco');
INSERT INTO equipos VALUES('Granada CF','Los Carmenes','2019/08/15','26','Robert Moreno','Manuel Carrasco','1912','Andalucia');
INSERT INTO equipos VALUES('Getafe CF','Alfonso Perez','2019/08/15','26','Michel','Alfredo Duro','1942','Madrid');
INSERT INTO equipos VALUES('Valencia CF','Mestalla','2019/08/15','26','Jose Bordalas','Peter Lim','1919','Comunidad Valenciana');
INSERT INTO equipos VALUES('Osasuna','El Sadar','2019/08/15','20','Yago Borruli','Kim Jon Ill','1923','Navarra');
INSERT INTO equipos VALUES('Athletic Club','San Mames','2019/08/15','26','Marcelino','Asier Illarramendi','1900','Pais Vasco');
INSERT INTO equipos VALUES('Levante UD','Ciutat Valencia','2019/08/15','26','Cristobal Garcia','Manuel Rivers','1932','Comunidad Valenciana');
INSERT INTO equipos VALUES('Real Valladolid','Jose Zorrilla','2019/08/15','26','Miguel Munoz','Ronaldo Nazario','1921','Castilla y Leon');
INSERT INTO equipos VALUES('SD Eibar','Ipurua','2019/08/15','26','Quique Setien','Aitor Igartiburu','1952','Pais Vasco');
INSERT INTO equipos VALUES('Real Betis Balompie','Benito Villamarin','2019/08/15','26','Manuel Pellegrini','Manuel Lopera','1907','Andalucia');
INSERT INTO equipos VALUES('Alaves','Mendizorroza','2019/08/15','26','Abelardo','Itxu Matamoros','1921','Pais Vasco');
INSERT INTO equipos VALUES('Celta de Vigo','Balaidos','2019/08/15','26','Coidet','Iago Aspas','1922','Galicia');
INSERT INTO equipos VALUES('Leganes','Butarque','2019/08/15','19','Javier Vargas','Jorge Duque','1932','Madrid');
INSERT INTO equipos VALUES('RCD Mallorca','Saint Noix','2019/08/15','26','Rafa Guerrero','David Guetta','1912','Islas Baleares');
INSERT INTO equipos VALUES('Espanyol','Cornella el Prat','2019/08/15','26','Fran Escriba','Gerard Pique','1904','Cataluña');
----LIGA---------------------------------------------------------------------------------------------------------------
INSERT INTO liga VALUES('1','Real Madrid','26','3','9','70','25');
INSERT INTO liga VALUES('2','FC Barcelona','25','6','7','86','38');
INSERT INTO liga VALUES('3','Atletico de Madrid','18','4','16','51','27');
INSERT INTO liga VALUES('4','Sevilla FC','19','6','13','54','34');
INSERT INTO liga VALUES('5','Villareal CF','18','14','6','63','49');
INSERT INTO liga VALUES('6','Real Sociedad','16','14','8','56','48');
INSERT INTO liga VALUES('7','Granada CF','16','14','8','52','45');
INSERT INTO liga VALUES('8','Getafe CF','14','12','12','43','37');
INSERT INTO liga VALUES('9','Valencia CF','14','13','11','46','53');
INSERT INTO liga VALUES('10','Osasuna','13','12','13','46','54');
INSERT INTO liga VALUES('11','Athletic Club','13','13','12','41','38');
INSERT INTO liga VALUES('12','Levante UD','14','13','12','47','53');
INSERT INTO liga VALUES('13','Real Valladolid','9','14','15','32','43');
INSERT INTO liga VALUES('14','SD Eibar','11','18','9','39','56');
INSERT INTO liga VALUES('15','Real Betis Balompie','17','11','7','48','60');
INSERT INTO liga VALUES('16','Alaves','10','19','9','34','59');
INSERT INTO liga VALUES('17','Celta de Vigo','7','15','16','37','49');
INSERT INTO liga VALUES('18','Leganes','8','18','12','30','51');
INSERT INTO liga VALUES('19','RCD Mallorca','9','23','6','40','65');
INSERT INTO liga VALUES('20','Espanyol','5','23','10','27','58');