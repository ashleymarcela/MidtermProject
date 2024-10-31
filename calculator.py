import logging
import sys
from plugins.add import add
from plugins.subtract import subtract
from history import HistoryManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def repl():
    history_manager = HistoryManager()
    history_manager.load_history()
    print("Welcome to the Advanced Python Calculator! Type 'exit' to quit.")
    print("Enter commands in the format: operation num1 num2 (e.g., 'add 5 10')")
    print("Type 'history' to view calculation history")
    
    while True:
        command = input(">>> ").strip()

        if command == 'exit':
            print('Goodbye!')
            break

        elif command == 'history':
            history = history_manager.display_history()
            print("Calculation History: ")
            print(history if not history.empty else "No history available.")
            continue

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


        history_manager.add_record(operation, num1, num2, result)
        history_manager.save_history()
        print(f"Result: {result}")

if __name__ == "__main__":
    repl()