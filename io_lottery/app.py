from flask import Flask, Response, request, jsonify

from io_lottery.controllers import AddUserController, AddUserRequest, GetUserController, UpdateUserController, DeleteUserController
from io_lottery.repositories import UserRepository
from io_lottery.views import UserView


class DBFlask(Flask):
    pass


app = Flask(__name__)


# @app.get("/users/<id>")
# def get_user(id: int) -> Response:
#     repository = UserRepository()
#     controller = GetUserController(repository=repository)
#     try:
#         controller.get(id)
#     except NotImplementedError:
#         pass
#     return Response(status=501)


# @app.post("/users")
# def add_user() -> Response:
#     repository = UserRepository()
#     controller = AddUserController(repository=repository)
#     controller.add(request=AddUserRequest(json=request.json))
#     return Response(response=jsonify(request.json), status=201)


# @app.put("/users/<id>")
# def update_user(id: int) -> Response:
#     repository = UserRepository()
#     controller = UpdateUserController(repository=repository)
#     controller.update(request=AddUserRequest(json=request.json))
#     return Response(response=jsonify(request.json), status=200)


# @app.patch("/users/<id>")
# def patch_user(id: int) -> Response:
#     repository = UserRepository()
#     controller = UpdateUserController(repository=repository)
#     controller.patch(request=AddUserRequest(json=request.json))
#     return Response(response=jsonify(request.json), status=200)


# @app.delete("/users/<id>")
# def delete_user(id: int) -> Response:
#     repository = UserRepository()
#     controller = DeleteUserController(repository=repository)
#     try:
#         controller.delete(id)
#     except NotImplementedError:
#         pass
#     return Response(status=204)

get_controller = GetUserController(
    repository=UserRepository()
)
post_controller = GetUserController(
    repository=UserRepository()
)
put_controller = GetUserController(
    repository=UserRepository()
)
patch_controller = GetUserController(
    repository=UserRepository()
)
delete_controller = GetUserController(
    repository=UserRepository()
)

app.add_url_rule("/users_new", view_func=UserView.as_view("users_new", controller=get_controller))
app.add_url_rule('/users/int:<id>', view_func=UserView.as_view())

# @app.get("/users/<id>")
# def get_user(id: int) -> Response:
#     return Response(status=501)

# @app.put("/users/<id>")
# def upgrade_user(id: int) -> Response:
#     raise NotImplementedError
