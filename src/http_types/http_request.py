class HttpRequest:
    body: dict
    param: dict

    def __init__(self, body: dict = None, param: dict = None) -> None:
        self.body = body
        self.param = param
