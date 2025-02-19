class HttpResponse:
    body: dict
    status_code: int

    def __init__(self, body: dict, status_code: int) -> None:
        self.body = body
        self.status_code = status_code
