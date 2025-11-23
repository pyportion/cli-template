from typer import Typer


def load_handlers(app: Typer) -> None:
    all_commands = []

    for command in all_commands:
        command(app)
