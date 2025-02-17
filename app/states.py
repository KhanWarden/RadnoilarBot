from aiogram.fsm.state import StatesGroup, State


class Lesson(StatesGroup):
    lesson_time = State()
