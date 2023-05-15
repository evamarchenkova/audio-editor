from pydub.exceptions import CouldntDecodeError


def handle_exception(exception):
    if isinstance(exception, FileNotFoundError):
        return 'Файл не найден'
    elif isinstance(exception, PermissionError):
        return 'Отказано в доступе'
    elif isinstance(exception, CouldntDecodeError):
        return 'Невозможно открыть файл'
    elif isinstance(exception, ValueError):
        return 'Неверный формат'
    else:
        return 'Возникла неизвестная ошибка'
