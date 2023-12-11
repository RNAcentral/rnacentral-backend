# SQLAlchemy models
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String

from database import Base


class Rna(Base):
    __tablename__ = "rna"

    id = Column(Integer)
    upi = Column(String, primary_key=True, index=True)
    timestamp = Column(Date)
    userstamp = Column(String)
    crc64 = Column(String)
    length = Column(Integer)
    seq_short = Column(String)
    seq_long = Column(String)
    md5 = Column(String)


class RnaPrecomputed(Base):
    __tablename__ = "rnc_rna_precomputed"

    id = Column(String, primary_key=True, index=True)
    taxid = Column(Integer, index=True)
    description = Column(String)
    upi = Column(String, ForeignKey("rna.upi"))
    rna_type = Column(String)
    update_date = Column(Date)
    has_coordinates = Column(Boolean)
    databases = Column(String)
    is_active = Column(Boolean)
    last_release = Column(Integer)
    short_description = Column(String)
