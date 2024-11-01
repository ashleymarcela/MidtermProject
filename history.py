'''file responsible for managing the calculations history in the Advanced Python Calculator'''
import pandas as pd

class HistoryManager:
    '''Saves, loads, and shows user the history of their calculations'''
    def __init__(self, filename = 'history.csv'):
        self.filename = filename
        '''Uses CSV file for storing history and initializes history manager'''
        self.history = pd.DataFrame(columns = ["operation", "operand1", "operand2", "result"])

    def add_record(self, operation, operand1, operand2, result):
        '''Addition of record of calculation to history'''
        new_record = {
            "operation": operation, 
            "operand1": operand1, 
            "operand2": operand2, 
            "result": result
        }

        if self.history.empty:
            self.history = pd.DataFrame([new_record])
        else:
            self.history = pd.concat(
                [self.history, pd.DataFrame([new_record])], ignore_index = True
            )

    def save_history(self):
        '''Responsible for loading the calculations history from CSV file'''
        self.history.to_csv(self.filename, index = False)

    def load_history(self):
        '''Responsible for loading the calculations history from a CSV file'''
        try:
            self.history = pd.read_csv(self.filename)
        except FileNotFoundError:
            self.history = pd.DataFrame(columns = ["operation", "operand1", "operand2", "result"])

    def clear_history(self):
        '''Resets the DataFrame and clears the calculation history'''
        self.history = pd.DataFrame(columns = ["operation", "operand1", "operand2", "result"])

    def display_history(self):
        '''Returns the history of calculations as a DataFrame'''
        return self.history
