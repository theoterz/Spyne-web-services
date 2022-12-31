from tkinter import *
from loginGUI import loginGUI
from ServiceGUI import serviceGUI
from zeep import Client


if __name__=='__main__':
    
    bank_client = Client('http://127.0.0.1:8000/?wsdl')

    login = loginGUI()
    login.createGUI(bank_client)

    id = login.getID()
    
    if(id != -1):
        service = serviceGUI()
        service.createGUI(id,bank_client)


