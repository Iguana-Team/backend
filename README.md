
## plain

```bash
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
