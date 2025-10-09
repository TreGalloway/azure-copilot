import click
from rich.console import Console

console = Console()

@click.command()
@click.argument('command')
def cli(command):
    """Process natural language commands"""
    console.print(f"You said: {command}")

    # Parse and handle the command
    if "list" in command.lower() and "resource" in command.lower():
        list_resources()
    elif "help" in command.lower():
        show_help()
    else:
        console.print("Command not recognized")

def list_resources():
    console.print("Listing your resources...", style="blue")
    # Your resource listing logic here

def show_help():
    console.print("Available commands: list resources, help")

if __name__ == '__main__':
    cli()
