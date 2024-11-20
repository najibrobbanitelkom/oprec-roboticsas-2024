# make a cli with a mimic AI named sebastian

accountList:list = [{
    'name': 'al',
    'ballance': 100_000_000_000
}]

class Account :
    def create(self, name, ballance = None):
        self.name = name
        self.ballance = ballance
        payload = dict(name = self.name, ballance = self.ballance)
        accountList.append(payload)
    
    def read(self, data):
        for item in accountList:
            if item["name"] == data: return item
        return False
    
    def update(self, data, name = None, ballance = None):
        if data in accountList: item = accountList.index(data)
        name = name if name != None else accountList[item]['name']
        ballance = ballance if ballance != None else accountList[item]['ballance']
        accountList[item] = dict(name = name, ballance = ballance)

class InputValidation:
    account = Account()
    def createAccount(self):
        name = input('input a name: ')
        if self.account.read(name) != False: 
            print('this name is already taken')
            return False
        deposit = int(input('input a number of money you want to deposit: '))
        self.account.create(name, deposit)
        print('account has been created')

    def login(self, data):
        user = self.account.read(data)
        if user == False: return print(f'there is no account with name like {data}')
        return user

    def withdraw(self, data, numberMoney:int):
        getMoney = numberMoney
        user = accountList[data]
        if user['ballance'] < getMoney: print('money is not enough')
        user['ballance'] -= getMoney
    
    def deposit(self, user, ballance):
        self.account.update(user, None, ballance)
        print(f'{ballance} has been added to your account')

class Sebastian :
    def __init__(self):
        print('this is your bank-system assistance Sebastian \nhow can i help you today?')
    
    def callCommand(self):
        validation = InputValidation()
        user = False
        while True:
            command = input()
            match(command):
                case "create account":
                    validation.createAccount()

                case "login":
                    user = validation.login(input('input your name: '))
                    if user != False: print(f'its nice to see you again sir {user['name']}')

                case "deposit":
                    if user == False: 
                        print('sorry but you have to login first') 
                        continue
                    validation.deposit(user, input('input a deposit: '))

                case "get ballance":
                    if user == False: 
                        print('sorry but you have to login first') 
                        continue
                    print(f'your ballance is {user['ballance']} right now')

                case "exit":
                    break

                case "help":
                    print("""chose one of the command below :
                            login              login to existing account
                            create account     make a new account
                            deposit            make a deposit for an existing account
                            get ballance       chakeing ballance on a existing account
                            exit               close the program""")
                    
                case _:
                    print('please type a command or type help to see command list')

def main():
    sebas = Sebastian()
    sebas.callCommand()

main()