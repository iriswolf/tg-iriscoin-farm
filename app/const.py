README_URL = 'https://github.com/iriswolf/tg-iriscoin-farm/blob/master/README.md'
WAIT_TIME_BEFORE_SEND_CMD = 4 * 3600 + 15


class IrisCommands:
    farm = 'фарма'


class LogMessages:

    class Debug:
        ...

    class Info:
        wait_seconds = "Ожидаю '{}' секунд "
        send_message_to_iris = "Отправляю ирису комманду: '{}'"

    class Warning:
        ...

    class Error:
        invalid_channel_name = (
            "Передано неверное короткое имя канала ирис бота. "
            "Измените переменную 'IRIS_CHANNEL_SHORTNAME' в '.env' файле, "
            f"либо перечитайте ещё раз инструкцию {README_URL!r} "
            "и проверьте правильно ли вы всё настроили."
        )
