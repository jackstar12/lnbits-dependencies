from fastapi import APIRouter

from lnbits.db import Database

db = Database("ext_dependencies")

dependencies_ext: APIRouter = APIRouter(prefix="/dependencies", tags=["dependencies"])


from .views_api import *  # noqa: F401,F403
