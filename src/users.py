from typing import Optional

from fastapi import Response, status, APIRouter


router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"],
)

@router.get(
    "/",
    tags = ["Users"],
    summary = "Endpoint to retrieve users",
    response_description = "List of users",
)
def get_users(response: Response,
              user_id: Optional[str] = None,
              user_name: Optional[str] = None,
              email: Optional[str] = None,
              first_name: Optional[str] = None,
              last_name: Optional[str] = None,
              age: Optional[int] = None,
    ):
    # TODO: Try adding multiple query params without bloating function parameters list but maintaining validation
    #  (maybe Pydantic model?)
    """
    Endpoint to retrieve users with request parameters.

    **user_id**: optional. Filter parameter
    """
    response.status_code = status.HTTP_200_OK
    users = [{"user_id": user_id} for _ in range(10)]

    return users


@router.get(
    "/{user_id}",
    tags = ["Users"],
    summary = "Endpoint to retrieve user by ID",
    response_description = "User object",
)
def get_user(response: Response, user_id: str):
    """
    Endpoint to retrieve user info by user_id.

    **user_id**: required. Path parameter
    """
    exists = 0 < int(user_id) < 100  # TODO: rework with actual implementation for exists check
    if not exists:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"User with {user_id=} not found"}
    response.status_code = status.HTTP_200_OK
    return {"user_id": user_id}