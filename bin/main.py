from db import refresh

def main():
    func_dict = {"1": refresh, '2': main }
    print("-")
    print("-")
    print("-")
    print("-")
    print("-")
    print("-")
    print("-")
    print("-")
    print("Welcome to Python Fraud Risk App")
    print("Select from the list of options:")
    print("-")
    print("-")
    print("1. Refresh Data")
    print("2. Address Distance")
    print("-")
    print("-")
    user_response = input("What would you like to do? Select from the list above:  ")
    func_dict[user_response]()
    try:
        print(user_response)
    finally:
        print("Close")

