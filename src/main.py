from fastapi import FastAPI

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate

app = FastAPI(
    title="Secret Santa"
)




# uusers = [
#     {"id":0, "gifts": [{'id':0,'gift_name':'phone'}], "name":"Rus"},
#     {"id":1, "gifts": [{'id':0,'gift_name':'phone'},{'id':1,'gift_name':'car'}], "name":"Ted"},
# ]



# class Gift(BaseModel):
#     id: int
#     gift_name: str

# # -----------_SANT
# class User(BaseModel):
#     id: int
#     name: str
#     gifts: List[Gift] 


# @app.get("/users/{user_id}", response_model=List[User])
# def get_users(user_id: int):
#     return [user for user in uusers if user.get("id") == user_id]


# @app.post("/add_gifts/{user_id}", response_model=List[Gift])
# def add_gifts(gift: List[Gift], user_id: int):
#     uusers[user_id]["gifts"].extend(gift)
#     return list(uusers[user_id]["gifts"])


# fastapi_users = fastapi_users.FastAPIUsers[User, int](
#     get_user_manager,
#     [auth_backend],
# )





app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)