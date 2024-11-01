'''Advanced Python Calculator'''
import logging
from plugins.add import add
from plugins.subtract import subtract
from history import HistoryManager

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

'''enables users to interact with the calculator through the command line'''
def repl():
    '''Running th repl look for the calculator allows users to provide input for calculations.'''
    history_manager = HistoryManager()
    history_manager.load_history()
    logger.info("History loaded.")
    print("Welcome to the Advanced Python Calculator! Type 'exit' to quit.")
    print("Enter commands in the format: operation num1 num2 (e.g., 'add 5 10')")
    print("Type 'history' to view calculation history")
    while True:
        command = input(">>> ").strip()

        if command == 'exit':
            print('Goodbye!')
            break

        if command == 'history':
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
            logger.warning("Unknown command '%s'", operation)
            continue

        if operation == 'add':
            result = add(num1, num2)
            logger.info("Performed addition: %f + %f = %f", num1, num2, result)
        elif operation == 'subtract':
            result = subtract(num1, num2)
            logger.info("Performed subtraction: %f - %f = %f", num1, num2, result)
        else:
            logger.warning("Unknown command '%s'", operation)
            continue


        history_manager.add_record(operation, num1, num2, result)
        history_manager.save_history()
        print(f"Result: {result}")

if __name__ == "__main__":
    repl()
