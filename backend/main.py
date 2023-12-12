from database import SessionLocal
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Annotated

import models
import schemas

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/rna/{id}", response_model=schemas.RnaPrecomputed, response_model_by_alias=False)
async def read_rna_precomputed(id: str, db: db_dependency):
    rna_precomputed = db.query(models.RnaPrecomputed).filter(models.RnaPrecomputed.id == id).first()
    if not rna_precomputed:
        raise HTTPException(status_code=404, detail="RNA not found")
    return rna_precomputed


@app.get("/rna/{upi}/xrefs", response_model=list[schemas.Xref], response_model_by_alias=False)
async def read_rna_precomputed(upi: str, db: db_dependency, skip: int = 0, limit: int = 10):
    xrefs = db.query(models.Xref).filter(models.Xref.upi == upi).offset(skip).limit(limit).all()
    if not xrefs:
        raise HTTPException(status_code=404, detail=f"No xref found for {upi}")
    return xrefs
