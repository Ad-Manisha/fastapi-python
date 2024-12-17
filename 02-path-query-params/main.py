from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test():
    return {'msg': 'test'}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "msg": "Here is your item."}

@app.get("/users/{user_name}")
def read_user_profile(user_name):
    return {"username": user_name, "msg": "You have successfully created your account."}

# http://localhost:8000/search?keyword=phone&category=electronics

@app.get("/search")
def search_items(keyword: str, category: str):
    return {
        "keyword": keyword,
        "category": category,
        "message": "Search Results!"
    }

