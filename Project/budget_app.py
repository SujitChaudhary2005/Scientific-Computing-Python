class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ''
        for entry in self.ledger:
            desc = entry['description'][:23].ljust(23)
            amt = f"{entry['amount']:.2f}".rjust(7)
            items += f'{desc}{amt}\n'
        total = f'Total: {self.get_balance():}'
        return title + items + total
    

def create_spend_chart(categories):
    category_names = []
    spending = []
    
    for category in categories:
        category_names.append(category.name)
        total = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                total += abs(entry['amount'])
        spending.append(total)
    
    total_spent = sum(spending)
    percentages = [(s / total_spent) * 100 for s in spending]
    rounded_percentages = [int(p // 10) * 10 for p in percentages]
    
    chart = 'Percentage spent by category\n'
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + '| '
        for percent in rounded_percentages:
            if percent >= i:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
    
    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'
    max_length = max(len(name) for name in category_names)
    for i in range(max_length):
        line = '     '
        for name in category_names:
            if i < len(name):
                line += name[i] + '  '
            else:
                line += '   '
        if i < max_length - 1:
            line += '\n'
        chart += line
        
    return chart

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(900, "deposit")
food.withdraw(105.55, "groceries")

clothing.deposit(500, "deposit")
clothing.withdraw(50.00, "clothes")

auto.deposit(1000, "deposit")
auto.withdraw(200.00, "gas")

print(food)
print(clothing)
print(auto)
print('\n',create_spend_chart([food, clothing, auto]))