from factory import DictFactory
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyFloat

from io_lottery.app import add_user, get_user, update_user, delete_user, patch_user, app


class UserPayloadFactory(DictFactory):
    name = FuzzyText()
    last_name = FuzzyText()
    email = FuzzyText()
    age = FuzzyInteger(low=0)
    essays_count = FuzzyInteger(low=0)
    rating = FuzzyFloat(low=0)


def test_returns_get_user() -> None:
    payload = UserPayloadFactory()
    with app.test_request_context(path="/users", method='GET', json=payload):
        actual = get_user()
    assert actual.json == payload


def test_returns_sent_user() -> None:
    payload = UserPayloadFactory()
    with app.test_request_context(path="/users", method='POST', json=payload):
        actual = add_user()
    assert actual.json == payload


def test_returns_update_user() -> None:
    payload = UserPayloadFactory()
    with app.test_request_context(path="/users", method='PUT', json=payload):
        actual = update_user()
    assert actual.json == payload


def test_returns_patch_user() -> None:
    payload = UserPayloadFactory()
    with app.test_request_context(path="/users", method='PATCH', json=payload):
        actual = patch_user()
    assert actual.json == payload


def test_returns_delete_user() -> None:
    payload = UserPayloadFactory()
    with app.test_request_context(path="/users", method='DELETE', json=payload):
        actual = delete_user()
    assert actual.json == payload


def test_returns_unimplemented() -> None:
    actual = get_user()
    assert actual.status_code == 501
