"""Кастомные ошибки."""


class APIStatusCodeError(Exception):
    """Ошибка статус кода."""

    pass


class APIResponseError(Exception):
    """Ошибка response."""

    pass


class TelegramError(Exception):
    """Ошибка Telegram."""

    pass


class TypeError(Exception):
    """Ошибка Telegram."""

    pass


class KeyError(Exception):
    """Ошибка ключа."""

    pass
