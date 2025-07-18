# Weather_Docker

Создайте чат бота в телеграмме с помощью @BotFather с уникальным именем и идентификатором, который вставьте в переменную BOT_TOKEN в файле run.py

Создайте учетную запись на https://openweathermap.org/, сгенерируйте API Key и вставьте в переменную APPID в файле run.py

Установите на хосте Docker по официальной документации, выбрав необходимый дистрибутив: https://docs.docker.com/engine/install/

Выполните последовательно команды, находясь в директории с Dockerfile: "docker build -t weatherbot ." и "docker run --name weatherbot --restart="always" -d weatherbot"
