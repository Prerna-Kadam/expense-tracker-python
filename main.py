from datetime import datetime
expenses = []#list of all expenses(kharcha)in form of dict. ye list of dictionary hogi jo keyvalue pair legi date,category,description,amount ye sab store krne ke liye.

print("WELCOME TO EXPENSE TRACKER💸🪙 💵")


while True:
    print("=====Menu=====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Amount spend(kharcha)")
    print("4. Exit")

    choice = input("Enter your choice(1-4) : ")

    # Validate Menu Choice
    if not choice.isdigit():
        print("Please enter a valid number.")
        continue

    choice = int(choice)

#1.Add Expense
    if choice == 1:
        
        # Date Validation
        while True:
            date = input("Enter Date (DD_MM_YYYY): ")

            try:
                datetime.strptime(date, "%d_%m_%Y")
                break
            except ValueError:
                print(" Invalid Date Format! Example: 15_07_2026")

        # Category Validation
        while True:
            category = input("Enter Category (Food, Travel, Shopping, Books): ").strip()

            if category == "":
                print(" Category cannot be empty.")
            else:
                break

        # Description Validation
        while True:
            description = input("Enter Description: ").strip()

            if description == "":
                print(" Description cannot be empty.")
            else:
                break

        # Amount Validation
        while True:

            amount = input("Enter Amount (₹): ")

            try:
                amount = float(amount)

                if amount <= 0:
                    print(" Amount must be greater than 0.")
                    continue

                break

            except ValueError:
                print(" Please enter a valid amount.")

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)

        print("\n Expense Added Successfully!")


#2. View All Expenses
    elif choice == 2:
        if (len(expenses))==0:
            print("No Expenses Added. Jao pehle khrcha karo.")
        else:
            print("=======This is your expense=======")
            count = 1
            for eachexpense in expenses: #eachkharcha
                print(f"Expense Number {count} -> {eachexpense["date"]}, {eachexpense["category"]},{eachexpense["description"]}, {eachexpense["amount"]}")
                count = count + 1

#3. View Total Amount spend(kharcha)
    elif choice == 3:
        total = 0
        for eachexpense in expenses:
            total = total + eachexpense["amount"]

        print("Total Expense = ",total)

#4. Exit
    elif choice == 4:
        print("\n🙏 Thank you for using Expense Tracker.")
        print("Have a Great Day!")
        break

    else:
        print("Invalid Choice! Please select between 1 and 4.")