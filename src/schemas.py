from pydantic import BaseModel


class NpmPackageLicense(BaseModel):
    text: str

    class Config:
        orm_mode = True


class NpmPackageLicenseCreate(NpmPackageLicense):
    owner: str
    package: str

    class Config:
        orm_mode = True
