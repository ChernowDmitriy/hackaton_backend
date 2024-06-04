from starlette import status

from core.exceptions import BaseHTTPException

SignatureVerificationFailed = BaseHTTPException(
    msg="Ошибка авторизации. Токен не найден или просрочен",
    status_code=status.HTTP_401_UNAUTHORIZED,
)

LoginFailedException = BaseHTTPException(
    msg="Неправильный логин или пароль",
    status_code=status.HTTP_400_BAD_REQUEST,
)

RefreshTokenFailedException = BaseHTTPException(
    msg="Доступ запрещен",
    status_code=status.HTTP_403_FORBIDDEN,
)

UserNotFound = BaseHTTPException(
    msg="Пользователь не найден",
    status_code=status.HTTP_404_NOT_FOUND,
)

AccessForbiddenException = BaseHTTPException(
    msg="Доступ запрещен",
    status_code=status.HTTP_403_FORBIDDEN
)

UserAlreadyExistsException = BaseHTTPException(
    msg="Пользователь с такой почтой уже зарегистрирован",
    status_code=status.HTTP_400_BAD_REQUEST
)
