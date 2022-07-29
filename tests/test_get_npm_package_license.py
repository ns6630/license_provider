from main import get_npm_package_license, app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_npm_package_license_was_received(db):
    db_license = get_npm_package_license(owner="facebook", package="react",
                                         db=db)
    print(db_license)
    assert db_license != ""
