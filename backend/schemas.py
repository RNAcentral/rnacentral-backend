# Pydantic models
from datetime import date, datetime
from pydantic import BaseModel


class Rna(BaseModel):
    upi: str
    timestamp: date
    userstamp: str
    crc64: str
    length: int
    seq_short: str
    seq_long: str
    md5: str


class RnaPrecomputed(BaseModel):
    id: str
    taxid: int
    description: str
    upi: str
    rna_type: str
    update_date: date
    has_coordinates: bool
    databases: str
    is_active: bool
    last_release: int
    short_description: str


class Xref(BaseModel):
    id: int
    db: int
    accession: str
    created: int
    last: int
    upi: str
    version_i: int
    deleted: str
    timestamp: datetime
    userstamp: str
    version: int
    taxid: int
