from fastapi import FastAPI

from app1.document import Document

documents: list[Document] = [
    Document(0, 'First', 'Content1'),
    Document(1, 'Second', 'Content2')
]

app = FastAPI()
##########Prometheus
# from prometheus_fastapi_instrumentator import Instrumentator
#
#
# @app.on_event("startup")
# async def startup():
#     Instrumentator().instrument(app).expose(app)


#################Jaeger
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

resource = Resource(attributes={
    SERVICE_NAME: "docs-service"
})

jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831,
)

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(jaeger_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

FastAPIInstrumentor.instrument_app(app)

####################

from sqlalchemy.orm import Session
from app1.sql_app import crud, schemas
from app1.sql_app.database import SessionLocal
from fastapi import Depends, HTTPException


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def addDocument(content:CreateDocModel):
#     id = len(documents)
#     documents.append(Document(id,content.title,content.body))
#     return id

@app.get("/doc/docs", response_model=schemas.SQLDocumentCreate)
async def getAllDocs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    documents = crud.get_docs(db, skip, limit)
    return documents


# @app.get("/doc/docs")
# async def getAllDocs():
#     return documents

@app.post("/doc/docs", response_model=schemas.SQLDocumentCreate)
async def postDoc(document: schemas.SQLDocumentBase, db: Session = Depends(get_db)):
    db_document = crud.get_docs_by_id(db, title=document.title)
    if (db_document):
        raise HTTPException(status_code=400, detail="Title already exist")
    return crud.add_doc(db=db, document=document)


@app.get("/doc/docs/{id}", response_model=schemas.SQLDocumentCreate)
async def getDocsById(id: int, db: Session = Depends(get_db)):
    db_document = crud.get_docs_by_id(db, document_id=id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_document


@app.get("/__health_check")
async def getHealthDocServ():
    return
