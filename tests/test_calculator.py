import pytest
from plugins.add import add
from plugins.subtract import subtract
from history import HistoryManager

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(2.5, 1.5) == 1.0

def test_history_manager():
    history_manager = HistoryManager()

    history_manager.add_record('add', 2, 3, 5)
    assert not history_manager.history.empty
    assert len(history_manager.history) == 1

    history_manager.save_history()

    history_manager.load_history()
    assert len(history_manager.history) == 1

    history_manager.clear_history()
    assert history_manager.history.empty