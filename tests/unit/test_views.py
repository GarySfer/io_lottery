from unittest.mock import Mock

import pytest
from flask.views import MethodView

from io_lottery.controllers import GetUserController
from io_lottery.views import UserView


@pytest.fixture
def controller_get() -> Mock:
    return Mock(GetUserController)


def controller_post() -> Mock:
    return Mock(GetUserController)


def controller_put() -> Mock:
    return Mock(GetUserController)


def controller_patch() -> Mock:
    return Mock(GetUserController)


def controller_delete():
    return Mock(GetUserController)


@pytest.fixture
def user_view(controller) -> UserView:
    return UserView(get_user_controller=controller)


def test_user_view_is_subclass_for_method_view(user_view: UserView) -> None:
    assert isinstance(user_view, MethodView)


def test_user_view_has_post_method(user_view: UserView) -> None:
    with pytest.raises(NotImplementedError):
        user_view.post()


def test_user_view_get(user_view: UserView, controller_get) -> None:
    user_view.get(1)
    assert controller_get.get.call_count > 0


def test_user_view_post(user_view: UserView, controller_post) -> None:
    user_view.post(1)
    assert  controller_post.post.call_count > 0

def test_user_view_put(user_view: UserView, controller_put) -> None:
    user_view.put(1)
    assert  controller_put.put.call_count > 0

def test_user_view_patch(user_view: UserView, controller_patch) -> None:
    user_view.patch(1)
    assert controller_patch.patch.call_count > 0


def test_user_view_delete(user_view: UserView, controller_delete) -> None:
    user_view.delete(1)
    assert controller_delete.delete.call_count > 0
