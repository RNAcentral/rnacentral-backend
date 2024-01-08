from database import SessionLocal
from debug_toolbar.middleware import DebugToolbarMiddleware
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Annotated

import models
import schemas

app = FastAPI(debug=True)
app.add_middleware(
    DebugToolbarMiddleware,
    panels=["debug_toolbar.panels.sqlalchemy.SQLAlchemyPanel"],
)


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
    data = (
        db.query(models.RnaPrecomputed, models.Rna)
        .join(models.Rna, models.RnaPrecomputed.upi == models.Rna.upi)
        .filter(models.RnaPrecomputed.id == id).first()
    )
    if not data:
        raise HTTPException(status_code=404, detail="RNA not found")

    db_precomputed, db_rna = data
    sequence = db_rna.seq_short if db_rna.seq_short else db_rna.seq_long

    response = schemas.RnaPrecomputed(
        id=db_precomputed.id,
        taxid=db_precomputed.taxid,
        description=db_precomputed.description,
        upi=db_precomputed.upi,
        rna_type=db_precomputed.rna_type,
        update_date=db_precomputed.update_date,
        has_coordinates=db_precomputed.has_coordinates,
        databases=db_precomputed.databases,
        is_active=db_precomputed.is_active,
        last_release=db_precomputed.last_release,
        short_description=db_precomputed.short_description,
        length=db_rna.length,
        sequence=sequence.replace("T", "U").upper(),
        md5=db_rna.md5
    )

    return response


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
