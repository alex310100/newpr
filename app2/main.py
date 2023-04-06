from fastapi import FastAPI, HTTPException
from app2.Templates import Templates

template: list[Templates] = [
    Templates(0, 'First_Temp', 'Content1,Content1'),
    Templates(1, 'Second_Temp', 'Content2,Content2')
]

app = FastAPI()


@app.get("/doc/templates")
async def getAllDocs():
    return template


@app.get("/doc/templates/{id}")
async def getDocsById(id: int):
    result = [item for item in template if item.id == id]
    if len(result) > 0:
        return result[0]

    raise HTTPException(status_code=404, detail="Templates not found")
