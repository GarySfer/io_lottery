from flask import jsonify, request, Response
from flask.views import MethodView
from io_lottery.controllers import GetUserController, AddUserController, AddUserRequest, UpdateUserController, \
    DeleteUserController
from io_lottery.repositories import UserRepository


class UserView(MethodView):

    def __init__(self, get_controller: GetUserController, post_controller: GetUserController, put_controller: GetUserController, patch_controller: GetUserController, delete_controller: GetUserController) -> None:
        self.get_controller = get_controller
        self.post_controller = post_controller
        self.put_controller = put_controller
        self.patch_controller = patch_controller
        self.delete_controller = delete_controller

    def get(self, id):
        try:
            user = self.get_controller.get(id)
            return jsonify(user), 501
        except NotImplementedError:
            pass

    def post(self) -> None:
        controller = self.post_controller
        controller.add(request=AddUserRequest(json=request.json))
        return jsonify(request.json), 201

    def put(self) -> None:
        controller = self.put_controller
        controller.update(request=AddUserRequest(json=request.json))
        return jsonify(request.json), 200

    def patch(self, id):
        controller = self.patch_controller
        controller.patch(request=AddUserRequest(json=request.json))
        return jsonify(request.json), 200

    def delete(self, id):
        controller = self.delete_controller
        try:
            controller.delete(id)
        except NotImplementedError:
            pass
        return "", 204
