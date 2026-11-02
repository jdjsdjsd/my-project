from fastapi import APIRouter
from fastapi import HTTPException, status

from projectback.shemass import StatusResponse, UserResponse, User, Pet

router = APIRouter()

users_database = dict[str, User]()

pets_database = dict[int, Pet]()


@router.get("/status")
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")


@router.get("/users/{user_id}")
def get_user(user_id: int) -> UserResponse:
    return UserResponse(
        username="john_doe",
        email="john.doe@example.com",
        full_name="John Doe"
    )


@router.post("/signup", status_code=201)
def signup(user: User):
    global users_database

    if user.username in users_database:
        raise HTTPException(409)

    users_database[user.username] = user


@router.get("/user/{username}")
def get_user(username: str) -> UserResponse:
    if username not in users_database:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    user = users_database[username]

    return UserResponse(
        username=user.username,
        email=user.email,
        full_name=user.name
    )


@router.post("/pets", status_code=201)
def create_pet(pet: Pet):
    if pet.id in pets_database:
        raise HTTPException(status_code=409)

    pets_database[pet.id] = pet

    return pet


@router.get("/pets/{pet_id}")
def get_pet(pet_id: int) -> Pet:
    if pet_id not in pets_database:
        raise HTTPException(status_code=404)

    return pets_database[pet_id]


@router.get("/pets")
def get_all_pets() -> list[Pet]:
    return list(pets_database.values())