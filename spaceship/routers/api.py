from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {
        'Name': 'Violetta',
        'Last_name': 'Yukhnenko',
        'Age': 18,
        'Group_code': 'IM-31',
        'Year': 2,
        'Form of study': 'Full-time',
        'Email': 'yukhnenko.violetta@1ll.kpi.ua'
    }

@router.get("/matrix")
def matrix_multiply():
    a = np.random.rand(10, 10).tolist()
    b = np.random.rand(10, 10).tolist()
    product = (np.dot(a, b)).tolist()
    return {
        "matrix_a": a,
        "matrix_b": b,
        "product": product
    }