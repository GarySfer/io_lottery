from flask.views import MethodView


class UserView(MethodView):

    def __init__(self, controller):
        raise NotImplementedError

    def get(self, id):
        raise NotImplementedError

    # modyfikacja częściowa
    def patch(self, id):
        raise NotImplementedError

    def delete(self, id):
        raise NotImplementedError

    def put(self) -> None:
        raise NotImplementedError

    def post(self) -> None:
        raise NotImplementedError
