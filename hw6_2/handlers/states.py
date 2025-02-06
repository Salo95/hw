# from aiogram import Bot, Dispatcher, types, Router
# from aiogram.filters import Command
# from aiogram .fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.fsm.storage.memory import MemoryStorage
# import asyncio
# import json

# router = Router()

# class Form(StatesGroup):
#      name = State()
#      age = State()
#      number = State()

# @router.message(Form.name)
# async def ask_age(message: types.Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer("Введите возраст")
#     await state.set_state(Form.age)

# @router.message(Form.age)
# async def ask_number(message: types.Message, state: FSMContext):
#     await state.update_data(date=message.text)
#     await message.answer("Введите номер телефона")
#     await state.set_state(Form.number)

# @router.message(Form.number)
# async def finish_form(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     if message.text == data['number']:
#         await message.answer('Вы уже зарегистрированы')
#     else:
#         await message.answer(f'''Данные сохранены:
# Имя: {data['name']}
# Возраст: {data['age']}
# Номер телефона: {data['number']}''')
#     await state.clear()

from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import json

router = Router()

class Form(StatesGroup):
    name = State()
    age = State()
    number = State()

def save_user_data(user_id, data):
    try:
        with open('dataa.json', 'r') as file:
            users_data = json.load(file)
    except FileNotFoundError:
        users_data = {}

    users_data[user_id] = data

    with open('dataa.json', 'w') as file:
        json.dump(users_data, file, indent=4)

def get_user_data(user_id):
    try:
        with open('dataa.json', 'r') as file:
            users_data = json.load(file)
        return users_data.get(user_id)
    except FileNotFoundError:
        return None 

@router.message(Form.name)
async def ask_age(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите возраст")
    await state.set_state(Form.age)

@router.message(Form.age)
async def ask_number(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите номер телефона")
    await state.set_state(Form.number)

@router.message(Form.number)
async def finish_form(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    data = await state.get_data()

    saved_data = get_user_data(user_id)

    if saved_data:
        if message.text == saved_data['number']:
            await message.answer('Вы уже зарегистрированы')
        else:
            await message.answer(f'''Данные сохранены:
Имя: {saved_data['name']}
Возраст: {saved_data['age']}
Номер телефона: {saved_data['number']}''')
    else:
        data['number'] = message.text
        save_user_data(user_id, data)
        await message.answer(f'''Данные сохранены:
Имя: {data['name']}
Возраст: {data['age']}
Номер телефона: {data['number']}''')
    await state.clear()

