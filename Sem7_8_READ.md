Задача
Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. Под форматами понимаем структуру файлов, например, в файле на одной строке хранится одна часть записи, пустая строка - разделитель

Решение
Структура проекта состоит из 4 модулей:
1. Sem7_8_UI (User Interface). Пользователь вводит данные для дальнейшого сохранения в телефонном справочнике. В данном модюле присутствует проверка на количество символов в номере телефона, и проверка на число. Все четыре категории данных, а именно фамилия, имя, номер телефона и описание, сохраняются в списке info.
2. Sem7_8_PB_CSV (Comma Separated Values). Модуль создает файл .csv и записывает в него оглавление таблицы.
3. Sem7_8_PB_File. Содержит два метода для записи файла c расширениями .csv и .txt. В первом данные сохраняются через ';', во втором - через пустую строку части записи, и через две пустые строки целые записи. 
4. Sem7_8_PB_Main. Проверяет существует ли файл с расширением .csv. Если нет, то запускает модуль Sem7_8_PB_CSV создания файла с оглавлением таблицы. После этого вызываюся модуль записи Sem7_8_PB_File, который в свою очередь забирает информацию из UI.