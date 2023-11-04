from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
import requests
import random

API_KEY_NASA = 'RhxK0ebTfCn4rmXGfRCVryJc99g4ChlQrJBykCs6'
API_TOKEN: str = '6912551238:AAHxKoEcpN_NW2ePYw0ipwPbb9cQjqAjA8E'

in_rover = False
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


async def set_main_menu(bot: Bot):
    menu = [
        BotCommand(command='/help',
                   description='Список команд'),
        BotCommand(command='/info',
                   description='Описание'),
        BotCommand(command='/start',
                   description='Начало'),
        BotCommand(command='/image',
                   description='Получить фото с марса')]
    await bot.set_my_commands(menu)


@dp.message(Command(commands=["start"]))
async def start_command(message: Message):
    await message.answer('Напишите /help чтобы узнать список команд')


@dp.message(Command(commands=["help"]))
async def help_command(message: Message):
    await message.answer('/start - начать\n'
                         '/help - помощь\n'
                         '/image - фото с марса\n')


@dp.message(Command(commands=["image"]))
async def image_command(message: Message):
    await message.answer('Выбор:\n'
                         '/curiosity\n'
                         '/spirit\n'
                         '/opportunity\n')


@dp.message(Command(commands=["curiosity"]))
async def curiosity_command(message: Message):
    random_number = random.randint(1, 337)
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={random_number}&api_key={API_KEY_NASA}"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        photo_url = response.json()["photos"][random.randint(1, 1)]["img_src"]
        await message.answer(photo_url)
        return
    await message.answer('Слишком много запрсосов')


@dp.message(Command(commands=["spirit"]))
async def spirit_command(message: Message):
    random_number = random.randint(1, 337)
    url2 = f"https://api.nasa.gov/mars-photos/api/v1/rovers/spirit/photos?sol={random_number}&api_key={API_KEY_NASA}"
    f"sol={random.randint(1,1000)}&api_key={API_KEY_NASA}"
    response = requests.get(url2)
    print(response.status_code)
    if response.status_code == 200:
        photo_url = response.json()["photos"][random.randint(1, 1)]["img_src"]
        await message.answer(photo_url)
        return
    await message.answer('Количество запросов превышено')


@dp.message(Command(commands=["opportunity"]))
async def opportunity_command(message: Message):
    random_number = random.randint(1, 337)
    url3 = f"https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?sol={random_number}&api_key={API_KEY_NASA}"
    f"sol={random.randint(1,1000)}&api_key={API_KEY_NASA}"
    response = requests.get(url3)
    print(response.status_code)
    if response.status_code == 200:
        photo_url = response.json()["photos"][random.randint(1, 1)]["img_src"]
        await message.answer(photo_url)
        return
    await message.answer('Слишком много запрсосов')


@dp.message(Command(commands=["info"]))
async def info_command(message: Message):
    await message.answer('Ровер - это дистанционно управляемый,'
                         'роботизированный, моторизованный аппарат,'
                         'предназначенный для передвижения по поверхности'
                         'другой планеты (или другого небесного тела). '
                         '4 июля 1997 года марсоход NASA Pathfinder Sojourner '
                         'стал первым колесным роботом с Земли, совершившим '
                         'посадку на скалистую поверхность Марса. В настоящее '
                         'время на Марсе успешно осуществили посадку шесть '
                         'марсоходов; из них три аппарата (Curiosity и '
                         'Perseverance NASA и китайский Zhurong) продолжают '
                         'активно работать.\n\n'
                         'Curiosity - марсоход размером с автомобиль '
                         'исследующий кратер Гейл и гору Шарп на Марсе в '
                         'рамках миссии Марсианской научной лаборатории (MSL) '
                         'НАСА.[2] Curiosity был запущен с мыса Канаверал '
                         '(CCAFS) 26 ноября 2011 года в 15:02:00 UTC и '
                         'приземлился на Эолис Палус внутри кратера Гейл на '
                         'Марсе 6 августа 2012 года в 05:17:57 UTC. '
                         'Посадочная площадка Брэдбери находилась менее чем в '
                         '2,4 км (1,5 мили) от центра цели приземления '
                         'марсохода после перелета в 560 миллионов километров '
                         '(350 миллионов миль) .'
                         'Цели миссии включают исследование марсианского '
                         'климата и геологии, оценку того, предлагала ли '
                         'выбранная площадка внутри Гейла когда-либо условия '
                         'окружающей среды, благоприятные для микробной жизни '
                         '(включая исследование роли воды), и изучение '
                         'обитаемостипланеты в рамках подготовки к '
                         'исследованию человеком..\n\n'
                         'Spirit, также известный как MER-A (Марсоход для '
                         'исследования Марса – A) или MER-2, является '
                         'марсоходом-роботом, работавшим с 2004 по 2010 год.'
                         'Spirit проработал на Марсе 2208 солнц, или 3,3 '
                         'марсианских года (2269 дней; 6 лет 77 дней). Это был'
                         ' один из двух марсоходов в рамках миссии НАСА по '
                         'исследованию Марса, выполняемой Лабораторией '
                         'реактивного движения "Марсоход". Дух приземлился '
                         'успешно в ударный кратер Гусева на Марсе в 04:35 '
                         'мирового Земле 4 января 2004 года, за три недели до '
                         'его близнец, возможность (рок-B), который '
                         'приземлился на другой стороне планеты. Его название '
                         'было выбрано в результате спонсируемого НАСА '
                         'конкурса студенческих эссе. Марсоход застрял в '
                         '"песчаной ловушке" в конце 2009 года под углом, '
                         'который препятствовал подзарядке его батарей; его '
                         'последняя связь с Землей была 22 марта 2010 года.')


if __name__ == '__main__':
    dp.startup.register(set_main_menu)
    dp.run_polling(bot)