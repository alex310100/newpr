from sqlalchemy.orm import Session

from . import models, schemas


def get_docs_by_id(db: Session, document_id: int):
    return db.query(models.SQLDocument).filter(models.SQLDocument.id == document_id).first()


def get_docs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SQLDocument).offset(skip).limit(limit).all()


def add_doc(db: Session, document: schemas.SQLDocumentBase):
    db_document = models.SQLDocument(title=document.title, body=document.body)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document
