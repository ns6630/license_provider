from sqlalchemy.orm import Session

from src import models, schemas
from src.utils import get_expiration_timestamp


def read_actual_npm_package_license(db: Session, owner: str, package: str):
    return db.query(models.NpmPackageLicense).filter(
        models.NpmPackageLicense.owner == owner,
        models.NpmPackageLicense.package == package,
        models.NpmPackageLicense.received_at > get_expiration_timestamp()). \
        first()


def create_npm_package_license(db: Session,
                               data: schemas.NpmPackageLicenseCreate):
    db_license = models.NpmPackageLicense(owner=data.owner,
                                          package=data.package, text=data.text)
    db.add(db_license)
    db.commit()
    db.refresh(db_license)
    return db_license


def delete_npm_package_license(db: Session, owner: str, package: str):
    deleted_count = db.query(models.NpmPackageLicense).filter(
        models.NpmPackageLicense.owner == owner,
        models.NpmPackageLicense.package == package,
        models.NpmPackageLicense.received_at <= get_expiration_timestamp()). \
        delete()
    db.commit()
    return deleted_count
