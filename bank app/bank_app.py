"""
X Bank's App - Deposit, withdraw, check balance.
"""

class BankAccount(object):
  
  def __init__(self, name):
    self.name = name
    self.balance = 0.00
  
  def __repr__(self):
    print('X Bank')
    print('Account holder: %s' % self.name)
    print('Balance: %.2f EUR\n' % self.balance)
    self.command()
    return ''
  
  def command(self):
    print('< press 1 > DEPOSIT')
    print('< press 2 > WITHDRAW')
    print('< press 3 > EXIT\n')
    action = input('')
    print('')
    if action == '1':
      d_amount = input('Deposit amount (EUR): ')
      print('')
      self.deposit(d_amount)
    elif action == '2':
      if self.balance != 0:
        w_amount = input('Withdraw amount (EUR): ')
        print('')
        self.withdraw(w_amount)
      else:
        print('Withdrawal unavailable.')
        self.show_balance()
        self.back_menu()
        print(self)
    elif action == '3':
      print('See you soon!')
      return
    else:
      print('Invalid command. Try again!\n')
      self.back_menu()
      print(self)

  def show_balance(self):
    print('Account balance: %.2f EUR' % self.balance)

  def back_menu(self):
    input('\n< Press ENTER to return >\n')

  def deposit(self, amount):
    if amount.replace('.', '').isdigit():
      amount = float(amount)
      if amount <= 0:
        print('Invalid input. Enter amount above 0.')
        self.back_menu()
        d_amount = input('Deposit amount (EUR): ')
        print('')
        self.deposit(d_amount)
      else:
        print('%.2f EUR was deposited\n' % amount)
        self.balance += amount
        self.show_balance()
        self.back_menu()
        print(self)
    else:
      print('Invalid input. Enter a valid number.')
      self.back_menu()
      d_amount = input('Deposit amount (EUR): ')
      print('')
      self.deposit(d_amount)

  def withdraw(self, amount):
    if amount.replace('.', '').isdigit():
      amount = float(amount)
      if amount > self.balance:
        print('Invalid input. Amount exceeds your balance.')
        self.back_menu()
        w_amount = input('Withdraw amount (EUR): ')
        print('')
        self.withdraw(w_amount)
      elif amount <= 0:
        print('Invalid input. Enter amount above 0.')
        self.back_menu()
        w_amount = input('Withdraw amount (EUR): ')
        print('')
        self.withdraw(w_amount)
      else:
        print('%.2f EUR was withdrawn' % amount)
        print('')
        self.balance -= amount
        self.show_balance()
        self.back_menu()
        print(self)
    else:
      print('Invalid input. Enter a valid number.')
      self.back_menu()
      w_amount = input('Withdraw amount (EUR): ')
      print('')
      self.withdraw(w_amount)

def login():
  print('\nSIGN IN\n')
  while True:
    my_name = input('Name: ')
    my_surname = input('Surname: ')
    if my_name == '' or my_surname == '':
      print('')
      print('Input empty. Enter name and surname.\n')
    elif any(char.isdigit() for char in my_name + my_surname):
      print('')
      print('Invalid input. Name and surname cannot contain digits.\n')
    else:
      break

  full_name = my_name.capitalize() + ' ' + my_surname.capitalize()
  my_account = BankAccount(full_name)
  print('\nYou have successfully signed in!\n')
  print(my_account)
  print('')

def sign_in():
  print('Welcome to X Bank!')
  print('< press 1 > SIGN IN')
  print('< press 2 > OPEN ACCOUNT')
  print('< press 3 > EXIT\n')
  choice = input('')
  if choice == '1':
    login()
  elif choice == '2':
    print('\nService unavailable')
    print('Please visit X Bank\'s local branch.')
    input('\n< Press ENTER to return to menu >\n')
    sign_in()
  elif choice == '3':
    print('\nSee you soon!')
    return
  else:
    print('\nInvalid command!')
    input('\n< Press ENTER to return to menu >\n')
    sign_in()

sign_in()


