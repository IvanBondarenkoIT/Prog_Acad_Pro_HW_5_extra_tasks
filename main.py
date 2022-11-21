"""
1. Create a class that performs statistical processing of a text file - counting characters, words,
 sentences, etc. Determine the required attributes-data and attributes-methods in class for
 working with the text file.

2. Write a program for selling tickets to IT-events. Each ticket has a unique number and a price.
 There are four types of tickets: regular ticket, advance ticket
 (purchased 60 or more days before the event),
 late ticket (purchased fewer than 10 days before the event) and student ticket.
Additional information:
-advance ticket - discount 40% of the regular ticket price;
-student ticket - discount 50% of the regular ticket price;
-late ticket - additional 10% to the regular ticket price.
All tickets must have the following properties:
-the ability to construct a ticket by number;
-the ability to ask for a ticket’s price;
-the ability to print a ticket as a String.

3. Pizzeria offers pizza-of-the-day for business lunch.
 The type of pizza-of-the-day depends on the day of week.
 Having a pizza-of-the-day simplifies ordering for customers.
 They don't have to be experts on specific types of pizza.
 Also, customers can add extra ingredients to the pizza-of-the-day.
 Write a program that will form orders from customers."""
import text_file_handler
import tickets


def main():

    # Text File
    txt_proc = text_file_handler.TxtProcessor()
    print(f'Sentences - {txt_proc.sentences}, Words - {txt_proc.words}, Chars - {txt_proc.characters}')


    # Tickets
    kass = tickets.Tickets()

    kass.add_ticket(tickets.Ticket(12301, "advance"))
    kass.add_ticket(tickets.Ticket(12302, "advance"))
    kass.add_ticket(tickets.Ticket(12303, "advance"))
    kass.add_ticket(tickets.Ticket(12304, "regular"))
    kass.add_ticket(tickets.Ticket(12305, "regular"))
    kass.add_ticket(tickets.Ticket(12306, "regular"))
    kass.add_ticket(tickets.Ticket(12307, "student"))
    kass.add_ticket(tickets.Ticket(12308, "student"))
    kass.add_ticket(tickets.Ticket(12309, "late"))
    # kass.add_ticket(tickets.Ticket(12309, "late")) # KeyError
    # kass.add_ticket(tickets.Ticket("12309", "late")) # TypeError
    tic = kass.get_by_number(12301)
    print(f"Ticket{tic.number} have a price {tic.get_price()}")

    for i in kass:
        print(i)


if __name__ == "__main__":
    main()
