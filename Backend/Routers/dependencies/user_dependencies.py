from typing import Annotated

from fastapi import Depends
from Backend.models import Seller , User
from Backend.Routers.dependencies.security import seller_verify , admin_verify
from Backend.Routers.dependencies.db_dependencies import db_dependency



seller_dependency = Annotated[Seller , Depends(seller_verify)]
admin_dependency = Annotated[User , Depends(admin_verify)]

