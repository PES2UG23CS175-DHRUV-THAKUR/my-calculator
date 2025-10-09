import sys
import click

# Assuming a local calculator.py module provides these functions:
# add(a,b), subtract(a,b), multiply(a,b), divide(a,b),
# power(a,b), square_root(a)
from calculator import add, subtract, multiply, divide, power, square_root


@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation: str, num1: float, num2: float | None = None):
    """Simple calculator CLI."""
    try:
        op = operation.lower()

        if op == "add":
            _require_num2(op, num2)
            result = add(num1, num2)  # type: ignore[arg-type]
        elif op == "subtract":
            _require_num2(op, num2)
            result = subtract(num1, num2)  # type: ignore[arg-type]
        elif op == "multiply":
            _require_num2(op, num2)
            result = multiply(num1, num2)  # type: ignore[arg-type]
        elif op == "divide":
            _require_num2(op, num2)
            result = divide(num1, num2)  # type: ignore[arg-type]
        elif op == "power":
            _require_num2(op, num2)
            result = power(num1, num2)  # type: ignore[arg-type]
        elif op == "square_root":
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Nicely format numeric output
        if float(result).is_integer():
            click.echo(int(result))
        else:
            click.echo(f"{float(result):.2f}")

    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except ZeroDivisionError:
        click.echo("Error: division by zero")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


def _require_num2(op: str, num2: float | None):
    if num2 is None:
        raise ValueError(f"Operation '{op}' requires two numbers")


if __name__ == "__main__":
    calculate()
