# backend

### Необходимые переменные окружения:
#### Application
* **HOST** - Пример: 0.0.0.0
* **PORT** - Пример: 8000
* **WORKERS** - Пример: 1
* **RELOAD** - Пример: True
* **ENVIRONMENT** - Пример: dev
#### DB
* **DB_HOST**
* **DB_PORT**
* **DB_USER**
* **DB_PASS**
* **DB_BASE**
* **DB_ECHO**
#### Auth
* **ACCESS_TOKEN_EXPIRE**
* **REFRESH_TOKEN_EXPIRE**
#### Security
* **JWT_SECRET_KEY**
#### RabbitMQ
* **RABBIT_HOST**
* **RABBIT_PORT**
* **RABBIT_USER**
* **RABBIT_PASS**
* **RABBIT_VHOST**

### запуск:
docker-compose -f docker-compose.dev.yml up --build -d

### установка дампа
pg_restore -U <username> -d <new_database_name> -h <hostname> -p <port> <input_file>

P.S Извините, за неполную таблицу. Сегодня ночью взломали сервер и потребовали 400$ для восстановления данных. 
Восстановили основные данные необходимые для работы