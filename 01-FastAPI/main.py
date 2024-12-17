from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greetMessage():
    return {"messgae": "Hi ! Good Morning."}

dogs = ['golden retriever', 'beagle', 'labrador retriever', 'chihuahua', 'corgi', 'husky']

@app.get("/dogs")
def callDogs():
    return dogs


@app.get("/")
def hello_world():
    return {"msg": "Hello world!"}