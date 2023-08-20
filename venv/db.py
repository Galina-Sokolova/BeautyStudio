import sglite3 as sq

cursor = None
connection = None




async def db_start():#создание таблицы
    global cursor, connection
    connection = sq.connect('resourses/users.db')#соединение с БД, если БД не было, то connect создаст её
    cursor = connection.cursor()#создаем курсор, который помогает перемещаться по строчкам и по экрану БД
    cursor.execute(''' CREATE TABLE "clients" (
    	"tel_number"	TEXT NOT NULL UNIQUE,
    	"name"	INTEGER NOT NULL,
    	"master"	TEXT,
    	PRIMARY KEY("tel_number"),
    	FOREIGN KEY("master") REFERENCES "masters"("tel_number")
    );''')#создаем таблицу клиенты
    cursor.execute(''' CREATE TABLE "masters" (
	"tel_number"	TEXT NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"status"	INTEGER DEFAULT 1,
	"rate"	INTEGER DEFAULT 10,
	"image"	TEXT NOT NULL,
	PRIMARY KEY("tel_number")
    );''')#создаст таблицу мастеров
    connection.commit()


async def create_client(client):
    tel_number_client = client['tel']
    result = cursor.execute(
        f'Select 1 from clients where tel_number=={tel_number_client}').fetchone()  # отдаст 1 кортеж 1 клиента или None
    if not result:
        cursor.execute(f'Insert into clients values({client["tel"]}, {client["name"]},{client["master"]})')
        connection.commit()


async def get_masters():
    result = cursor.execute(
        f'Select * from masters where status==1').fetchall()  # получим список кортежей: имя мастера, тел. мастера, статус мастера
    return result
