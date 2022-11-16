NORMAL_TICKET_PRICE = 100
types_of_tickets = {"regular": 1, "advance": 0.6, "student": 0.5, "late": 1.1}


class TIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped):
            self.index = self.index + 1
            return self.wrapped[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


class Tickets:
    def __init__(self):
        self.numbers = []
        self.tickets = []

    def add_ticket(self, ticket):
        if isinstance(ticket, Ticket) and isinstance(ticket.number, int):
            if ticket.number not in self.numbers:
                self.numbers.append(ticket.number)
                self.tickets.append(ticket)
            else:
                raise KeyError
        else:
            raise TypeError

    def get_by_number(self, number):
        if isinstance(number, int):
            if number in self.numbers:
                idx = self.numbers.index(number)
                return self.tickets[idx]
            else:
                raise KeyError
        else:
            raise TypeError

    def __iter__(self):
        return TIterator(self.tickets)


class Ticket:
    def __init__(self, number, ticket_type):
        self.number = number
        self.type = ticket_type
        self.price = self.get_price()

    def get_price(self):
        return round(NORMAL_TICKET_PRICE * types_of_tickets[self.type], 2)

    def __str__(self):
        return f"Ticket № {self.number}. {self.type}. Price {self.price}"
