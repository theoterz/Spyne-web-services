from zeep import Client

def printMenu():
    print("======================")
    print("1.Withdrawal")
    print("2.Deposit")
    print("3.Show Balance")
    print("4.Exit")
    print("======================")

def getInput():
    service = 0
    while(service<1 or service>4):
        printMenu()
        service = int(input("Enter Choise:"))

    return service 


if __name__=='__main__':
    bank_client = Client('http://127.0.0.1:8000/?wsdl')
    id = -1
    while id == -1:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        id = bank_client.service.login(username, password)

    choise = getInput()
    while choise != 4:
        if choise == 1: 
            amount = input("Enter Amount: ")
            response = bank_client.service.withdrawal(id, amount)
        elif choise == 2:
            amount = input("Enter Amount: ")
            response = bank_client.service.deposit(id, amount)
        elif choise == 3:
            response = bank_client.service.showBalance(id)

        print(response)
        choise = getInput()
        
