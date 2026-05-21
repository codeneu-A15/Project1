from typing import Annotated

from fastapi import Depends
from Backend.models import Seller , User
from Backend.Routers.dependencies.security import seller_verify , admin_verify , get_current_user



seller_dependency = Annotated[Seller , Depends(seller_verify)]
admin_dependency = Annotated[User , Depends(admin_verify)]
customer_dependency = Annotated[User , Depends(get_current_user)]
