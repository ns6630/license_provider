# License provider

```
cp ./.env.default ./.env
```
```
python3 -m venv ./venv
```
```
source ./venv/bin/activate
```
```
pip install -r requirements.txt
```
```
dotenv run uvicorn main:app --reload
```
```
pytest
```