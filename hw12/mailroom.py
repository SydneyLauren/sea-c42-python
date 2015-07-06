

def mailroom(userinput='thank you'):
    fulldonorlist = {'Sydney Decoto': [20],
                     'Big Bird': [300, 400],
                     'John Doe': [1000],
                     'Jane Doe': [600, 50],
                     'Harry Potter': [20, 30, 40]}

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
        check = False
        # Initialize the donor list
        # donorlist = fulldonorlist[0]
        # If the user types list, print the names
        if userinput == 'list':
            for name in fulldonorlist:
                print(name)
            userinput = input("Enter Donor Name: ")

        if userinput != 'quit':
            # append list of donors with new name
            # donorlist.append(userinput)
            donorname = userinput
            check = userinput in fulldonorlist
            userinput = input("""\nPlease enter a donation \
amount or 'quit':\n\n""")
            donoramount = "none"
            while donoramount == "none":
                try:
                    donoramount = int(userinput)
                except ValueError:
                    print("Entry was not a number")

            n = []
            if donorname in fulldonorlist:
                n = fulldonorlist[(donorname)]
                n.append(donoramount)
                fulldonorlist[(donorname)] = n
            else:
                fulldonorlist[(donorname)] = [donoramount]
        else:
            break

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
    totaldonation = []
    averagedonation = []
    numdons = []
    for donor in fulldonorlist:
        totaldonation.append(sum(fulldonorlist[donor]))
        averagedonation.append((sum(fulldonorlist[donor]) /
                                len(fulldonorlist[donor])))
        numdons.append(len(fulldonorlist[donor]))

    sortdon = sorted(totaldonation)
    a = sorted(range(len(totaldonation)), key=lambda k: totaldonation[k])
    sortedlist = fulldonorlist  # somehow magically sort the data
    print('Name         | Total |  #  |   Average ')
    print('\n______________________________________________________')
    names = list(fulldonorlist.keys())
    for num in a:
        print(names[num], totaldonation[num],
              numdons[num], averagedonation[num], sep='\t')

    input('\nPress Enter to Continue ...')

