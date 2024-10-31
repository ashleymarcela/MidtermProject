import pandas as pd 

class HistoryManager:
    def __init__(self, filename = 'history.csv'):
        self.filename = filename
        self.history = pd.DataFrame(columns = ["operation", "operand1", "operand2", "result"])

    def add_record(self, operation, operand1, operand2, result):
        new_record = {"operation": operation, "operand1": operand1, "operand2": operand2, "result": result}
        self.history = pd.concat([self.history, pd.DataFrame([new_record])], ignore_index = True)

    def save_history(self):
        self.history.to_csv(self.filename, index = False)

    def load_history(self):
        try:
            self.history = pd.read_csv(self.filename)
        except FileNotFoundError:
            self.history = pd.DataFrame(columns = ["operation", "operand1", "operand2", "result"])

    def clear_history(self):
        self.history = pd.DataFrame(columns = ["operation", "operand1", "operand2", "result"])

    def display_history(self):
        return self.history 