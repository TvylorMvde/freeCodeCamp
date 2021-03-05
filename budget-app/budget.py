class Category:

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.spent = 0
        self.ledger = []

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -abs(amount), "description": description})
            self.balance -= amount
            self.spent += amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.ledger.append({"amount": -abs(amount), "description": f"Transfer to {category.name}"})
            category.ledger.append({"amount": amount, "description": f"Transfer from {self.name}"})
            self.balance -= amount
            self.spent += amount
            category.balance += amount
            return True
        return False

    def check_funds(self, amount):
        return False if amount > self.balance else True

    def __str__(self):
        title = self.name.center(30, "*")
        items = "\n".join([item['description'][:23].ljust(23) + "{:.2f}".format(item['amount']).rjust(7) for item in self.ledger])
        total = f"Total: {self.balance}"
        return title + "\n" + items + "\n" + total


def create_spend_chart(categories):

    chart_title = "Percentage spent by category\n"
    total_spent: float = sum(x.spent for x in categories)
    percentages = [(x.spent / total_spent) // 0.01 for x in categories]

    for p_value in range(100, -10, -10):
        chart_title += str(p_value).rjust(3, " ") + "|"
        for percentage in percentages:
            if percentage >= p_value:
                chart_title += " o "
            else:
                chart_title += " " * 3
        chart_title += " \n"

    chart_title += " " * 4 + "-" * 3 * len(percentages) + "-\n"
    longest_name = max(len(x.name) for x in categories)

    for char in range(longest_name):
        chart_title += " " * 4
        for name in categories:
            if char < len(name.name):
                chart_title += " " + name.name[char] + " "
            else:
                chart_title += " " * 3

        chart_title += " \n"

    chart_title = chart_title.rstrip() + " " * 2

    return chart_title