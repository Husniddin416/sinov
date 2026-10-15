# Cars API (FastAPI)

Mashinalar ro'yxati va CRUD amallari uchun FastAPI orqali yozilgan API.

## Mahalliy ishga tushirish (Local)

1. Kerakli kutubxonalarni o'rnatish:
   ```bash
   pip install -r requirements.txt
   ```

2. Loyihani ishga tushirish (8000-portda):
   ```bash
   python main.py
   ```
   yoki
   ```bash
   uvicorn main:app --reload --port 8000
   ```

3. Swagger hujjatlar: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## React Frontend bilan ulash

- **Portlar**:
  - React (CRA): `http://localhost:3000` yoki (Vite): `http://localhost:5173`
  - FastAPI: `http://localhost:8000`
  *(Ikkisi alohida portlarda ishlagani uchun hech qanday port to'qnashuvi bo'lmaydi)*.

- **CORS sozlamasi**:
  - `main.py` da `CORSMiddleware` ulandi, shuning uchun React'dan kelgan barcha GET, POST, PUT, DELETE so'rovlari muammosiz qabul qilinadi.

- **React kodida API ga ulanish**:
  ```javascript
  // Mahalliy (local) sinovda:
  const API_URL = "http://127.0.0.1:8000";

  // Render'ga deploy qilingandan so'ng:
  // const API_URL = "https://cars-api-xxxx.onrender.com";

  // Masalan:
  fetch(`${API_URL}/cars`)
    .then(res => res.json())
    .then(data => console.log(data));
  ```

---

## Render.com da 24/7 ishga tushirish sozlamalari

- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
