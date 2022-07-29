from sqlalchemy import Integer, Column, String

from src.database import Base
from src.utils import get_utcnow_timestamp


class NpmPackageLicense(Base):
    __tablename__ = "npm_package_license"
    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String)
    package = Column(String)
    text = Column(String)
    received_at = Column(Integer, default=get_utcnow_timestamp)
