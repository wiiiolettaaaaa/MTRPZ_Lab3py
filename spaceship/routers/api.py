from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {
        'Name': 'Violetta',
        ' Last_name': 'Yukhnenko',
        'Age': 18,
        'Group _code': 'IM-31'
    }
