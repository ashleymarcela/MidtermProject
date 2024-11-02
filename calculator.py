'''Advanced Python Calculator'''
import logging
from plugins.add import add
from plugins.subtract import subtract
from plugins.multiply import multiply
from plugins.divide import divide
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
        logger.debug("Operation: %s, Num1: %f, Num2: %f", operation, num1, num2)

        if operation == 'add':
            result = add(num1, num2)
            logger.info("Performed addition: %f + %f = %f", num1, num2, result)
        elif operation == 'subtract':
            result = subtract(num1, num2)
            logger.info("Performed subtraction: %f - %f = %f", num1, num2, result)
        elif operation == 'multiply':
            result = multiply(num1, num2)
            logger.info("Performed multiplication: %f * %f = %f", num1, num2, result)
        elif operation == 'divide':
            if num2 == 0:
                logger.error('Cannot divide by zero.')
                print("Error: Cannot divide by zero.")
                continue
            result = divide(num1, num2)
            logger.info("Performed division: %f / %f = %f", num1, num2, result)
        else:
            logger.warning("Unknown command '%s'", operation)
            continue


        history_manager.add_record(operation, num1, num2, result)
        history_manager.save_history()
        print(f"Result: {result}")

if __name__ == "__main__":
    repl()
