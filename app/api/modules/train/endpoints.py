from typing import Literal

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session
from app.db_utils import engine


from .models import *
from .schema import *

router = APIRouter(prefix="/trains", tags=["trains"])

