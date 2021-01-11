from affe_core.console.actions import ConsoleAction


class DemoConsoleAction(ConsoleAction):
    _desc = 'Demo Action'

    def __call__(self, *args, **kwargs) -> str:
        return 'Demo Action'
