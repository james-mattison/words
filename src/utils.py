green = lambda text: f"\033[0;32m{text}\033[0m"
underline = lambda text: f"\033[4m{text}\033[0m"
red = lambda text: f"\033[0;31m{text}\033[0m"
yellow = lambda text: f"\033[0;33m{text}\033[0m"
blue = lambda text: '\033[0;34m' + str(text) + '\033[0m'
cyan = lambda text: '\033[0;45m' + str(text) + '\033[0m'
bcyan = lambda text: u'\u001b[36;1m' + str(text) + u'\u001b[0m'
bold = lambda text: u'\u001b[1m\u001b[1m' + str(text) + u'\u001b[0m'
boldunderline = lambda text: u'\u001b[1m\u001b[4m' + str(text) + u'\u001b[0m'
boldreverse = lambda text: u'\u001b[1m\u001b[4m\u001b[7m' + str(text) + u'\u001b[0m'


class GameException(BaseException):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        print(red(f"GameException: {self.msg}!"))


def fail(text: str, fatal: bool = False):
    if not fatal:
        print(red(text))
    else:
        raise GameException(text)
