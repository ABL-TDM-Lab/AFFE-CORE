import sys
from abc import ABC
from typing import Any, Final, TextIO

from affe_core.console.actions import ConsoleAction
from affe_core.console.actions.demo_action import DemoConsoleAction


class Console(ABC):
    _in: Final[TextIO]
    _out: Final[TextIO]
    _actions: list[ConsoleAction]

    def __init__(
        self,
        actions: list[ConsoleAction],
        *,
        input_io: TextIO = sys.stdin,
        output_io: TextIO = sys.stdout,
    ):
        self._in = input_io
        self._out = output_io
        self._actions = sorted(actions, key=lambda action: action.serial)
        self._writeln("Hello!")

    def show_menu(self):
        self._writeln("Please Select an Action:")
        for action in self._actions:
            self._writeln(action)

    def _writeln(self, s: Any):
        self._out.write(f"{s}\n")


class CLIConsole(Console):
    def __init__(self):
        super().__init__([DemoConsoleAction(serial=1)])


console = CLIConsole()
console.show_menu()
