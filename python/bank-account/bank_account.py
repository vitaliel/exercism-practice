import threading

# More on threading:
# https://www.tutorialspoint.com/python/python_multithreading.htm

class BankAccount(object):
  def __init__(self):
    self.lock = threading.Lock()
    self.is_open = False
    self.balance = 0

  def get_balance(self):
    if self.is_open:
      return self.balance
    else:
      raise ValueError("Account is not open")

  def open(self):
    self.is_open = True

  def deposit(self, amount):
    if not self.is_open:
      raise ValueError("Account is closed")
    if amount <= 0:
      raise ValueError("Deposit amount should be greater than 0")
    self.lock.acquire()
    self.balance += amount
    self.lock.release()

  def withdraw(self, amount):
    if not self.is_open:
      raise ValueError("Account is closed")

    if amount <= 0:
      raise ValueError("Withdraw amount should be greater than 0")

    try:
      self.lock.acquire()
      if self.balance - amount >= 0:
        self.balance -= amount
      else:
        raise ValueError("Not enough funds in account")
    finally:
      self.lock.release()

  def close(self):
    self.is_open = False
