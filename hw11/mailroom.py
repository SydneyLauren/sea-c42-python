

def mailroom(userinput='thank you'):
    fulldonorlist = []
    while userinput != 'quit':
        userinput = input("""\nWelcome to Mailroom Madness\n
Choose from the following:\n\nT - Send a (T)hank You\n
R - Create a (R)eport\n\nquit - Quit the program\n\n""")

        if userinput == 'T':
            fulldonorlist = thankyou(userinput)
        elif userinput == 'R':
            createreport(fulldonorlist)
        elif userinput != 'quit':
            print('invalid entry')


# Prepare the thank you email
def thankyou(userinput):
    while userinput != 'quit':
        userinput = input("""\nPlease enter a name, or choose from the following:\n
list - Print a list of previous donors\n
quit - Return to main menu\n\n""")
        # Initialize the donor list
        donorlist = []
        # If the user types list, print the names
        if userinput == 'list':
            print(donorlist)
            userinput = input("Enter Donor Name: ")
        elif userinput != 'quit':
            # append list of donors with new name
            donorlist.append(userinput)
        else:
            break
            return(userinput)
        donorname = userinput
        # Promt for a donation amount
        donoramount = "none"

        while donoramount == "none":
            userinput = input("""\nPlease enter a donation \
amount or 'quit':\n\n""")

            try:
                donoramount = int(userinput)
                fulldonorlist = [donorlist, [donoramount]]
                return fulldonorlist
                print(fulldonorlist)
                break
            except ValueError:
                print("Entry was not a number")

        # Draft the email
        print('\nDear %s,\n\n' % donorname, 'Thank you so \
much for your kind donation of $%d.' % donoramount, 'We \
here at the Foundation for Homeless Whales greatly \
appreciate it. Your money will go towards creating new \
oceans on the moon for whales to live in.\n\n\
Thanks again,\n\nJim Grant\n\nDirector, F.H.W.')
        input('\nPress Enter to Continue ...')
        return donoramount
        break


def createreport(donoramount):
    print('        Name         |    Total    |  #  |   Average ')
    print('\n______________________________________________________')
    print('\nBill Gates           |     $100.00 |   1 |     $100.00')
    input('\nPress Enter to Continue ...')

