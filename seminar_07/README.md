## Погружение в Python (семинары)
### Урок 7. Файлы и файловая система

1.
* Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
* Первое число int, второе - float разделены вертикальной чертой.
* Минимальное число - -1000, максимальное - +1000.
* Количество строк и имя файла передаются как аргументы функции.

2.
* Напишите функцию, которая генерирует псевдоимена.
* Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
* Полученные имена сохраните в файл.

3.
* Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
* Перемножьте пары чисел. В новый файл сохраните имя и произведение:
    * если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
    * если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
* В результирующем файле должно быть столько же строк, сколько в более длинном файле.
* При достижении конца более короткого файла, возвращайтесь в его начало.

4.
* Создайте функцию, которая создаёт файлы с указанным расширением.

    Функция принимает следующие параметры:
    * расширение
    * минимальная длина случайно сгенерированного имени, по умолчанию 6
    * максимальная длина случайно сгенерированного имени, по умолчанию 30
    * минимальное число случайных байт, записанных в файл, по умолчанию 256
    * максимальное число случайных байт, записанных в файл, по умолчанию 4096
    * количество файлов, по умолчанию 42
* Имя файла и его размер должны быть в рамках переданного диапазона.

5.
* Доработаем предыдущую задачу.
* Создайте новую функцию которая генерирует файлы с разными расширениями.
* Расширения и количество файлов функция принимает в качестве параметров.
* Количество переданных расширений может быть любым.
* Количество файлов для каждого расширения различно.
* Внутри используйте вызов функции из прошлой задачи.

6.
* Дорабатываем функции из предыдущих задач.
* Генерируйте файлы в указанную директорию — отдельный параметр функции.
* Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
* Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

7.
* Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
* Каждая группа включает файлы с несколькими расширениями.
* В исходной папке должны остаться только те файлы, которые не подошли для сортировки.



