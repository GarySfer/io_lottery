from dataclasses import dataclass

from io_lottery.repositories import UserRepository


@dataclass
class AddUserRequest:
    json: dict


class AddUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def add(self, request: AddUserRequest) -> None:
        self._repository.add()
        print(request.json)


class GetUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def get(self, id: int):
        raise NotImplementedError


class UpdateUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def update(self, request: AddUserRequest) -> None:
        raise NotImplementedError

    def patch(self, request: AddUserRequest) -> None:
        # get user
        # modify user
        # update user
        raise NotImplementedError


class DeleteUserController:
    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    def delete(self, id: int) -> None:
        raise NotImplementedError
