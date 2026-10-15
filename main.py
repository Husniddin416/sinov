from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Cars API")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "Cars API muvaffaqiyatli ishlamoqda",
        "docs": "/docs"
    }


# Boshlang'ich mashinalar bazasi (1, 2, 3 va 4-id'li mashinalar bilan)
car_list = [
    {
        "id": 1,
        "name": "Cobalt",
        "price": 140000000.0,
        "description": "Oq rangli, mexanika",
        "state": "Yangi"
    },
    {
        "id": 2,
        "name": "Gentra",
        "price": 180000000.0,
        "description": "Qora rangli, avtomat",
        "state": "Ajoyib"
    },
    {
        "id": 3,
        "name": "Tracker",
        "price": 250000000.0,
        "description": "Qizil rangli, turbo",
        "state": "Ajoyib"
    },
    {
        "id": 4,
        "name": "Malibu",
        "price": 350000000.0,
        "description": "Qora rangli, Premier",
        "state": "Yangi"
    }
]

class Car(BaseModel):
    name: str
    price: float
    description: str
    state: str

# 1. GET - Barcha mashinalarni olish
@app.get("/cars")
def get_cars():
    return car_list

# GET - Bitta mashinani ID bo'yicha olish
@app.get("/cars/{car_id}")
def get_single_car(car_id: int):
    for car in car_list:
        if car["id"] == car_id:
            return car
    raise HTTPException(status_code=404, detail="Bunday id dagi mashina topilmadi")

# 2. POST - Yangi mashina qo'shish
@app.post("/cars")
def create_car(car: Car):
    # Avtomatik yangi ID yaratish (oxirgi element ID siga 1 qo'shamiz)
    new_id = car_list[-1]["id"] + 1 if car_list else 1
    
    new_car = {
        "id": new_id,
        "name": car.name,
        "price": car.price,
        "description": car.description,
        "state": car.state
    }
    car_list.append(new_car)
    return {
        "message": "Mashina muvaffaqiyatli qo'shildi",
        "car": new_car
    }

# 3. PUT - Mavjud mashina ma'lumotlarini o'zgartirish (yangilash)
@app.put("/cars/{car_id}")
def update_car(car_id: int, update_car: Car):
    for index, car in enumerate(car_list):
        if car["id"] == car_id:
            car_list[index] = {
                "id": car_id,
                "name": update_car.name,
                "price": update_car.price,
                "description": update_car.description,
                "state": update_car.state
            }
            return {
                "message": "Mashina ma'lumotlari muvaffaqiyatli yangilandi",
                "car_id": car_id,
                "car": car_list[index]
            }
    raise HTTPException(status_code=404, detail="Bunday id dagi mashina topilmadi")

# 4. DELETE - Mashinani o'chirish
@app.delete("/cars/{car_id}")
def delete_car(car_id: int):
    for index, car in enumerate(car_list):
        if car["id"] == car_id:
            deleted_car = car_list.pop(index)
            return {
                "message": "Mashina muvaffaqiyatli o'chirildi",
                "car": deleted_car
            }
    raise HTTPException(status_code=404, detail="Bunday id dagi mashina topilmadi")