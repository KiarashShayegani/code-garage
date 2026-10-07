from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home_page():
    return """
  <div style="padding: 2px 20px; font-family: system-ui">
    <h1 style="color: #5C6AC4;">Hello, World!</h1>
    <p>
      <a href="/api/hello" style="color: inherit;">Hello</a>
      </br>
      <a href="/api/names" style="color: inherit;">Names List</a>
    </p>
  </div>
"""
@app.get("/api/hello")
def hello():
  return {"message": "Hello there!"}

names_list =[
  {"id":1, "name":"Jason"},
  {"id":2, "name":"Lucia"},
  {"id":3, "name":"Raul"},
  {"id":4, "name":"Michael"},
  {"id":5, "name":"Franklin"}
]

@app.get("/api/names")
def all_names():
  return names_list

@app.get("/api/names/{pid}")
def single_name(pid: int):
  for person in names_list:
    if person["id"] == pid:
      return person
  return {"details": "Could not find the person with that pid!"}

@app.post("/api/names/{name}")
def add_person(name: str):
  try:
    new_person = {"id": random.randint(100,1000), "name": name}
    names_list.append(new_person)
    return new_person
  except:
    return {"details": "Could not add the person to the list!"}

@app.delete("/api/names/{pid}")
def del_person(pid: int):
  for person in names_list:
    if person.get("id") == pid:
      # def person
      names_list.remove(person)
      return person
  return {"details": "Could not delete the person from the list"}
  
@app.patch("/api/names/{info}")
def edit_person(pid: int, new_name: str):
  for person in names_list:
    if person["id"] == pid:
      person["name"] = new_name
      return person
  return {"details": "Could not edit the person on the list"}

