from aiogram.contrib.fsm_storage.memory import MemoryStorage#ременный буфер
from aiogram.dispatcher import FSMContext#конечный автомат
from aiogram.dispatcher.filters.state import StatesGroup,State#класс от которого будем наследоваться


buffer=MemoryStorage()#объект буфера

class UserProfile(StatesGroup):
    #блоки которые попадают в буфер
    name = State()
    telphone_number = State()
    master = State()#кортеж из 2 эл-в, тел № мастера и время записи


dispatcher = None
def start_FSM(db):
    global  dispatcher
    dispatcher = db

