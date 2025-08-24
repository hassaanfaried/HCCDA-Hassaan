_balance_record = {}  # customer_id -> balance


def check_balance(customer_id):
    """Return current balance of a user."""
    return _balance_record.get(customer_id, 0)


def deposit(customer_id, amount):
    """Deposit money into the account."""
    if amount <= 0:
        print("Invalid deposit amount.")
        return
    _balance_record[customer_id] = _balance_record.get(customer_id, 0) + amount
    print(f"Deposited {amount}. New balance: {_balance_record[customer_id]}")


def withdraw(customer_id, amount):
    """Withdraw money if sufficient funds exist."""
    if amount <= 0:
        print("Invalid withdrawal amount.")
        return

    balance = _balance_record.get(customer_id, 0)
    if balance >= amount:
        _balance_record[customer_id] = balance - amount
        print(f"Withdrew {amount}. Remaining balance: {_balance_record[customer_id]}")
    else:
        print("Insufficient balance")
