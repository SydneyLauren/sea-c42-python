

def mailroom(userinput='thank you'):
    fulldonorlist = [["Sydney Decoto", "Big Bird"], [[20], [300, 400]]]
    while userinput != 'quit':
        userinput = input("""\nWelcome to Mailroom Madness\n
Choose from the following:\n\nT - Send a (T)hank You\n
R - Create a (R)eport\n\nquit - Quit the program\n\n""")

        if userinput == 'T':
            fulldonorlist = thankyou(userinput, fulldonorlist)
        elif userinput == 'R':
            createreport(fulldonorlist)
        elif userinput != 'quit':
            print('invalid entry')


# Prepare the thank you email
def thankyou(userinput, fulldonorlist):
    while userinput != 'quit':
        userinput = input("""\nPlease enter a name, or choose from the following:\n
list - Print a list of previous donors\n
quit - Return to main menu\n\n""")
        # Initialize the donor list
        donorlist = fulldonorlist[0]
        # If the user types list, print the names
        if userinput == 'list':
            print(donorlist)
            userinput = input("Enter Donor Name: ")
        elif userinput != 'quit':
            # append list of donors with new name
            donorlist.append(userinput)
        else:
            break

        donorname = userinput
        # Promt for a donation amount
        donoramount = "none"

        while donoramount == "none":
            userinput = input("""\nPlease enter a donation \
amount or 'quit':\n\n""")

            try:
                donoramount = int(userinput)
                fulldonorlist[0].append(donorname)
                fulldonorlist[1].append(donoramount)
                print(fulldonorlist[1])
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
        return fulldonorlist
        break


def createreport(fulldonorlist):
    # read through full donor list
    for i in len(fulldonorlist[0]):
        fulldonorlist[0][i]

    print(fulldonorlist)

    print('        Name         |    Total    |  #  |   Average ')
    print('\n______________________________________________________')
    print('\nBill Gates           |     $100.00 |   1 |     $100.00')
    input('\nPress Enter to Continue ...')
