import logging
import sys
from plugins.add import add
from plugins.subtract import subtract
from history import HistoryManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def repl():
    print("Welcome to the Advanced Python Calculator! Type 'exit' to quit.")
    while True:
        command = input(">>> ").strip()

        if command == 'exit':
            print('Goodbye!')
            break

        parts = command.split()
        if len(parts) != 3:
            logger.warning("Invalid command format. Use 'operation num1 num2'")
            continue

        operation, num1, num2 = parts[0], parts[1], parts[2]

        try:
            num1, num2 = float(num1), float(num2)
        except ValueError:
            logger.error("Please enter valid numbers for calculation.")
            continue

        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        else:
            logger.warning(f"Unknown command '{operation}'")
            continue

        print(f"Result: {result}")

if __name__ == "__main__":
    repl()