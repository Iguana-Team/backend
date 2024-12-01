
## plain

```bash
создать .env файл и заполнить его
Пример заполненного файла:
    POSTGRES_HOST=postgres
    POSTGRES_PORT=5432
    POSTGRES_DB=mtslink
    POSTGRES_PASSWORD=postgres
    POSTGRES_USERNAME=postgres

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python main.py
```

## docker

```bash
docker compose up --build

docker exec -it backend-iguana-api-1 alembic upgrade head #только при первом запуске
```
