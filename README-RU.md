## Hallo, ich bin Nikolai Fedorov.
### Игра Зейка для гимназии FDG.


Название файла    | Содержание файла
------------------|----------------------
pics              | папка с картинками
sound             | папка со звуками
fdg_snake_main.py | python-программа

Стек технологий:  pygame 2.6.1

Class/fun              | Description
-----------------------|----------------------
fun load_image         | функция загружает картинку и устанавливает её размер
class Game             | класс игры, описывает основные параметры игры: игровое поле, картинки, звуки, шрифт
&nbsp; &nbsp; &nbsp; &nbsp; fun init         | инициализация класса
&nbsp; &nbsp; &nbsp; &nbsp; fun main               | главный метод/цикл игры
&nbsp; &nbsp; &nbsp; &nbsp; fun pickup             | если попала голова на яблоко добавляет счёт и риcует новое яблоко
&nbsp; &nbsp; &nbsp; &nbsp; fun text_on_screen     | выводит текст на экран
&nbsp; &nbsp; &nbsp; &nbsp; fun gameover           | устонавливает self.game_play = False если голова змеи попала на тело змеи
class Snake            | класс змеи, хранит параметры змеи
&nbsp; &nbsp; &nbsp; &nbsp; fun init               | инициализация класса
&nbsp; &nbsp; &nbsp; &nbsp; fun move               | метод движения змеи, проверяет нажатие клавиш и меняет направление движения


Скриншот Игры:  
<img width="405" alt="Screenshot 2025-04-19  Snake" src="https://github.com/user-attachments/assets/cef5d5bf-5f61-40a1-ae37-43f062128a21" />
