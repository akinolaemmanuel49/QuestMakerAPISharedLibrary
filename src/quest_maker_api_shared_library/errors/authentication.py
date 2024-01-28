class AuthenticationError(Exception):
    def __init__(self, detail: str) -> None:
        self.detail = detail


class ScopeError(AuthenticationError):
    def __init__(self, detail: str) -> None:
        super().__init__(f'Insufficient scope. Required scope: {detail}')


class ExpiredTokenError(AuthenticationError):
    def __init__(self, detail: str = 'Token has expired. Please re-authenticate.') -> None:
        super().__init__(detail)


class InvalidTokenError(AuthenticationError):
    def __init__(self, detail: str) -> None:
        super().__init__(f'Invalid token. Reason: {detail}')
