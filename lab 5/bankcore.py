branch_id = 2057
_users_info = {}   # customer_id -> {"name": ..., "password": ...}
_user_counter = 0  # keeps track of number of users created


def create_account(name, password):
    """Register a new user and return customer_id."""
    global _user_counter
    _user_counter += 1
    customer_id = f"{branch_id}-{_user_counter}"
    _users_info[customer_id] = {"name": name, "password": password}
    print(f"Account created successfully! Your Customer ID is: {customer_id}")
    return customer_id


def login(customer_id, password):
    """Validate login credentials."""
    if customer_id in _users_info and _users_info[customer_id]["password"] == password:
        print(f"Login successful! Welcome {_users_info[customer_id]['name']}.")
        return True
    else:
        print("Invalid login")
        return False


def get_users_info():
    """Helper function to access users dictionary (used by accounts)."""
    return _users_info
