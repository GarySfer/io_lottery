import pytest
from flask import Flask

from eat_it.app import DBFlask

@pytest.fixture
def db_flask() -> DBFlask:
    return DBFlask("dummy_import_name")

def test_db_flask_is_subclass_of_flask(db_flask: DBFlask) -> None:
    db_flask = DBFlask("dummy_import_name")
    assert isinstance(db_flask, Flask)

    def test_raises_on_run_method() -> None:
        with pytest.raises(NotImplementedError):
            db_flask.run()