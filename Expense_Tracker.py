expenses = []
income = []

print("Welcome! Let's track your paisa 💸")
print("Press the menu number to choose what you want to do.")

while True:
    print("\nMenu:")
    print("1: Add Income")
    print("2: Add Expense")
    print("3: Show Total Income/Expenses/Balance")
    print("4: Category-wise Karcha Report")
    print("5: See All Income Entries")
    print("6: See All Expenses")
    print("7: Delete Wrong Income")
    print("8: Delete Wrong Expense")
    print("9: Bas, Exit!")

    ch = input("Bhai kya karna hai? : ")
    
    if ch == "1":
        try:
            amount = float(input("Kitna kamaaya? : "))
            desc = input("Kis se/kyun? Thoda batao: ")
            income.append({"amount": amount, "desc": desc})
            print("Income add ho gaya! Good job! 👍")
        except:
            print("Arre bhai, sahi number daalo.")

    elif ch == "2":
        try:
            amount = float(input("Kitna kharch kiya? : "))
            desc = input("Kya tha ye karcha? : ")
            category = input("Kis category me daloge? (Food, Travel, etc.): ")
            expenses.append({"amount": amount, "desc": desc, "category": category})
            print("Expense add ho gaya! Paisa gya... 😅")
        except:
            print("Bhai number sahi daalo.")

    elif ch == "3":
        total_income = sum(i["amount"] for i in income)
        total_expenses = sum(e["amount"] for e in expenses)
        print(f"Total Kamaai: {total_income}")
        print(f"Total Karch: {total_expenses}")
        print(f"Bacha hua: {total_income - total_expenses}")

    elif ch == "4":
        cats = {}
        for e in expenses:
            cat = e["category"]
            cats[cat] = cats.get(cat, 0) + e["amount"]
        print("\nCategory-wise Report:")
        for cat, total in cats.items():
            print(f"{cat}: {total}")

    elif ch == "5":
        print("\nIncome Entries:")
        if not income:
            print("Kuch bhi nahi kamaaya abhi tak 😆")
        for idx, i in enumerate(income):
            print(f"{idx+1}. {i['amount']} | {i['desc']}")

    elif ch == "6":
        print("\nExpense Entries:")
        if not expenses:
            print("Aaj kharcha nahi hua abhi tak 😎")
        for idx, e in enumerate(expenses):
            print(f"{idx+1}. {e['amount']} | {e['desc']} | {e['category']}")

    elif ch == "7":
        print("\nIncome Entries:")
        for idx, i in enumerate(income):
            print(f"{idx+1}. {i['amount']} | {i['desc']}")
        idx = int(input("Kaunsa hataana hai? Number batao: ")) - 1
        if 0 <= idx < len(income):
            income.pop(idx)
            print("Ho gaya delete, set hai!")
        else:
            print("Galat number daala bhai.")

    elif ch == "8":
        print("\nExpense Entries:")
        for idx, e in enumerate(expenses):
            print(f"{idx+1}. {e['amount']} | {e['desc']} | {e['category']}")
        idx = int(input("Kaunsa hataana hai? Number batao: ")) - 1
        if 0 <= idx < len(expenses):
            expenses.pop(idx)
            print("Expense delete ho gaya, paisa bach gaya 😃")
        else:
            print("Galat number daala bhai.")

    elif ch == "9":
        print("Bye! Apna paisa dhang se sambhalna. ✌️")
        break
    else:
        print("Menu me diya hua number daalo! 🙏")