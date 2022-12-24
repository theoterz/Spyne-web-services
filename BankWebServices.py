from spyne import ServiceBase, Application, Float
from spyne.decorator import rpc
from spyne.model.primitive import Integer, Unicode
import psycopg2
from database import Database
from decimal import *
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class BankWebServices(ServiceBase):

    global db
    db = Database()

    @rpc(Unicode, Unicode, _returns=Integer)
    def login(self, name, password):
   
        id = db.authenticateUser(name, password)

        return id
    
    @rpc(Integer, Float, _returns=Unicode)
    def withdrawal(self, id, amount):

        return db.withdrawal(id, amount)
    
    @rpc(Integer, Float, _returns=Unicode)
    def deposit(self, id, amount):

        return db.deposit(id, amount)
    
    @rpc(Integer, _returns=Unicode)
    def showBalance(self, id):

        return db.showBalance(id)

    


application = Application([BankWebServices], 'spyne.bank.services.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()