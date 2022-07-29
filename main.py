import requests
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src.constants import BRANCH_NAMES, LICENSE_FILE_NAMES, NPM_LICENSE_STORAGE
from src.database import SessionLocal, engine
from src import crud, models, schemas
from src.schemas import NpmPackageLicenseCreate

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def check_status():
    return {"message": "Ok"}


@app.get("/npm")
def get_npm_package_license(owner: str, package: str,
                            db: Session = Depends(get_db)):
    license_from_db = crud.read_actual_npm_package_license(db, owner, package)

    if license_from_db:
        return license_from_db.text
    else:
        crud.delete_npm_package_license(db, owner, package)

    for branch in BRANCH_NAMES:
        for license_file_name in LICENSE_FILE_NAMES:
            response = requests.get(
                f'{NPM_LICENSE_STORAGE}/'
                f'{owner}/{package}/{branch}/{license_file_name}')
            if response.status_code == 200:
                license_obj = NpmPackageLicenseCreate(owner=owner,
                                                      package=package,
                                                      text=response.text)
                license_obj = crud.create_npm_package_license(db, license_obj)
                return license_obj.text
    raise HTTPException(status_code=404)
