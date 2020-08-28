from __future__ import annotations
from typing import Callable
import threading


def threadlock(func: Callable[[BankAccount, int], None]) -> Callable:
    def wrapper(*args):
        with args[0]._lock:
            return func(*args)

    return wrapper


def is_open(func: Callable) -> Callable:
    def wrapper(*args):
        if not args[0].state:
            raise ValueError("Account closed")
        return func(*args)

    return wrapper


def is_positive_amount(func: Callable[[BankAccount, int], None]) -> Callable:
    def wrapper(*args):
        if args[1] < 0:
            raise ValueError("Cannot adjust by anegative amount")
        return func(*args)

    return wrapper


class BankAccount(object):
    def __init__(self) -> None:
        self.state: bool = False
        self._lock: threading.Lock = threading.Lock()

    def open(self) -> None:
        if self.state:
            raise ValueError("Account already open")
        self.state = True
        self.balance: int = 0

    @is_open
    def get_balance(self) -> int:
        return self.balance

    @threadlock
    @is_open
    @is_positive_amount
    def deposit(self, amount: int) -> None:
        self.balance += amount

    @threadlock
    @is_open
    @is_positive_amount
    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient balance: cannot withdraw")
        self.balance -= amount

    @is_open
    def close(self) -> None:
        self.state = False
