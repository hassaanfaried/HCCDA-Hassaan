from banking_app import bankcore, accounts


def main():
    print("=== Welcome to Hassaan Fareed Bank ===")

    while True:
        print("\nSelect an option:")
        print("1. Create Account")
        print("2. Login to Account")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            name = input("Enter your name: ")
            password = input("Create a password: ")
            customer_id = bankcore.create_account(name, password)
            print(f"Please save your Customer ID: {customer_id}")

        elif choice == "2":
            customer_id = input("Enter Customer ID: ")
            password = input("Enter Password: ")

            if bankcore.login(customer_id, password):
                while True:
                    print("\n--- Banking Menu ---")
                    print("1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Check Balance")
                    print("4. Logout")

                    option = input("Choose option (1-4): ")

                    if option == "1":
                        amt = int(input("Enter amount to deposit: "))
                        accounts.deposit(customer_id, amt)

                    elif option == "2":
                        amt = int(input("Enter amount to withdraw: "))
                        accounts.withdraw(customer_id, amt)

                    elif option == "3":
                        balance = accounts.check_balance(customer_id)
                        print(f"Your balance is: {balance}")

                    elif option == "4":
                        print("Logged out successfully!")
                        break
                    else:
                        print("Invalid choice. Try again.")

        elif choice == "3":
            print("Thank you for using Hassaan Fareed Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
