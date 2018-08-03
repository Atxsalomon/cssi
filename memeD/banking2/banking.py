import webapp2
import jinja2
import os
from transaction import Transaction
import time

jinja_loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
jinja_current_directory = jinja2.Environment(
loader=jinja_loader,
extensions=['jinja2.ext.autoescape'],
autoescape=True)

def get_balance():
    transactions = Transaction.query().fetch()

    balance = 0
    for trans in transactions:
        balance += trans.amount
    return balance

class BankingHandler(webapp2.RequestHandler):
    def get(self):
        home_template=jinja_current_directory.get_template(
        'templates/banking.html')
        my_dict={'current_balance': get_balance()}
        self.response.write(
        home_template.render(my_dict))

class MoneyHandler(webapp2.RequestHandler):
    def post(self):
        home_template=jinja_current_directory.get_template(
        'templates/banking.html')
        amount = int(self.request.get('amount'))
        transaction = Transaction(amount=amount)
        transaction.put()
        time.sleep(1)
        my_dict={'current_balance': get_balance()}
        self.response.write(
        home_template.render(my_dict))













app = webapp2.WSGIApplication([
('/banking',BankingHandler),
('/money',MoneyHandler)
], debug=True)
