from fastapi import FastAPI, HTTPException

app = FastAPI()

persons = [
    {"id": 1, "name": "ahmed", "age": 24, "Gender": "Male"},
    {"id": 2, "name": "mahmoud", "age": 22, "Gender": "Male"},
    {"id": 3, "name": "aliaa", "age": 22, "Gender": "FeMale"}
]

@app.get("/person")
def get_all_persons():
    return {"persons": persons}

@app.get("/person/{id}")
def get_person(id: int):
    for person in persons:
        if person["id"] == id:
            return {"person": person}
    raise HTTPException(status_code=404, detail="Person Not Exist")
