from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class SQLDocument(Base):
    __tablename__ = "docs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
