import sglite3 as sq

cursor = None
connection = None


async def db_start():
    global cursor, connection
    connection = sq.connect('resourses/users.db')
    cursor = connection.cursor()


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
