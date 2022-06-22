

class MessageBaseError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class NoConnection(MessageBaseError):
    def __init__(self) -> None:
        super().__init__(f'Connection not valid')
