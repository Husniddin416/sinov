# Cars API (FastAPI)

Mashinalar ro'yxati va CRUD amallari uchun FastAPI orqali yozilgan API.

## Mahalliy ishga tushirish (Local)

1. Kerakli kutubxonalarni o'rnatish:
   ```bash
   pip install -r requirements.txt
   ```

2. Loyihani ishga tushirish:
   ```bash
   uvicorn main:app --reload
   ```

3. Swagger hujjatlar: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Render.com da 24/7 ishga tushirish sozlamalari

- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
