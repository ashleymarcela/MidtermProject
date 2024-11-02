'''File Responsible for unit testing the Advanced Python Calculator and the HistoryManager Class'''
from plugins.add import add
from plugins.subtract import subtract
from plugins.multiply import multiply
from plugins.divide import divide
from history import HistoryManager

def test_add():
    '''Testing the add function using a variety of cases'''
    assert add(2, 3) == 5.0, "Expected output: 5.0"
    assert add(-1, 1) == 0.0, "Expect output: 0.0"
    assert add(0, 0) == 0.0, "Expected output: 0.0"
    assert add(1.5, 2.5) == 4.0, "Expected output: 4.0"

def test_subtract():
    '''Testing the subtract function using a variety of cases'''
    assert subtract(5, 3) == 2.0, "Expected output: 2.0"
    assert subtract(0, 0) == 0.0, "Expected output: 0.0"
    assert subtract(-1, -1) == 0.0, "Expected output: 0.0"
    assert subtract(2.5, 1.5) == 1.0, "Expected output: 4.0"

def test_multiply():
    '''Testing the multiply function using a variety of cases'''
    assert multiply(2, 3) == 6.0, "Expected output: 6.0"
    assert multiply(-1, 5) == -5.0, "Expect output: -5.0"
    assert multiply(0, 100) == 0.0, "Expected output: 0.0"
    assert multiply(1.5, 2) == 3.0, "Expected output: 3.0"

def test_divide():
    '''Testing the divide function using a variety of cases'''
    assert divide(6, 3) == 2.0, "Expected output: 2.0"
    assert divide(-6, 3) == -2.0, "Expect output: -2.0"
    assert divide(1.5, 0.5) == 3.0, "Expected output: 3.0"

    try:
        divide(5,0)
        assert False, "Expected ValueError for division by zero"
    except ValueError:
        pass

def test_history_manager():
    '''Testing functionality of the HistoryManager class'''
    history_manager = HistoryManager()

    history_manager.add_record('add', 2, 3, 5)
    assert not history_manager.history.empty, "history shouldn't be empty after adding a record"
    assert len(history_manager.history) == 1, "history should only have 1 record"

    history_manager.save_history()

    history_manager.load_history()
    assert len(history_manager.history) == 1, "history should have only 1 record after loading"

    history_manager.clear_history()
    assert history_manager.history.empty, "after clearing, history should be empty"

if __name__ == '__main__':
    test_add()
    test_subtract()
    test_history_manager()
    print("All tests passed!")
