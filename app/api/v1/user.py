from fastapi import APIRouter

from app.api.v1.views.user import (
    UserListView,
    UserDetailView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
)

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

router.add_api_route("/", UserListView.as_view(), methods=["GET"])
router.add_api_route("/{user_id}", UserDetailView.as_view(), methods=["GET"])
router.add_api_route("/", UserCreateView.as_view(), methods=["POST"])
router.add_api_route("/{user_id}", UserUpdateView.as_view(), methods=["PUT"])
router.add_api_route("/{user_id}", UserDeleteView.as_view(), methods=["DELETE"])
