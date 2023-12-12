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


@app.get("/rna/{id}", response_model=schemas.RnaPrecomputed)
async def rna_precomputed(id: str, db: db_dependency):
    """
    Unique RNAcentral Sequence.
    """
    rna = db.query(models.RnaPrecomputed).filter(models.RnaPrecomputed.id == id).first()
    if not rna:
        raise HTTPException(status_code=404, detail="RNA not found")
    return rna


@app.get("/rna/{upi}/xrefs/{taxid}", response_model=list[schemas.Xref])
async def xrefs(upi: str, taxid: int, db: db_dependency, skip: int = 0, limit: int = 10):
    """
    List of cross-references for a particular RNA sequence in a specific species
    """
    results = db.query(models.Xref).filter(
        models.Xref.upi == upi, models.Xref.taxid == taxid
    ).offset(skip).limit(limit).all()

    if not results:
        raise HTTPException(status_code=404, detail=f"No xref found for {upi}_{taxid}")

    return results
