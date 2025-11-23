from typing import Dict

from cli.core import Logger


class CommandBase:
    def __init__(self, **kwargs: Dict[str, str]) -> None:
        self.logger = Logger(quiet=False)
