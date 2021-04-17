bought_tickets = []


class Tickets:
    def __init__(self):
        self.amount = 500

    def print_amount(self):
        print(self.amount)


class Customer:

    def __init__(self, seat, row):
        self.seat = seat
        self.row = row


class Seller:

    def sell(self, customer, tickets):
        if [customer.seat, customer.row] not in bought_tickets:
            bought_tickets.append([customer.seat, customer.row])
            tickets.amount -= 1
            print('Thanks for choosing us, your place is ' + str([customer.seat, customer.row]))
        else:
            print('You have to choose another seat')


ticket = Tickets()
customer_1 = Customer(19, 5)
customer_2 = Customer(19, 5)
seller = Seller()
seller.sell(customer_1, ticket)
seller.sell(customer_2, ticket)
customer_2 = Customer(18, 5)
seller.sell(customer_2, ticket)
ticket.print_amount()
print(bought_tickets)

