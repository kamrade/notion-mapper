import typer
from programs.hello import my_hello, my_goodbye
from programs.scope import my_scope
import os


os.system('clear')
app = typer.Typer()


@app.command()
def hello(name: str):
    my_hello(name)


@app.command()
def goodbye(name: str, formal: bool = False):
    my_goodbye(name, formal)


@app.command()
def scope():
    my_scope()


if __name__ == "__main__":
    app()

