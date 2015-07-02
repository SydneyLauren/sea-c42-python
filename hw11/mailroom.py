

def mailroom(userinput='thank you'):
    fulldonorlist = [["Sydney Decoto", "Big Bird", "John Doe", "Jane Doe",
                      "Cher"], [[20], [300, 400], [1000], [600, 50],
                    [20, 30, 40]], []]

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
        donorlist = fulldonorlist[0]
        # If the user types list, print the names
        if userinput == 'list':
            print(donorlist)
            userinput = input("Enter Donor Name: ")
            check = userinput in fulldonorlist[0]
            if check:
                ind = fulldonorlist[0].index(userinput)
            else:
                fulldonorlist[0].append(userinput)
        elif userinput != 'quit':
            # append list of donors with new name
            # donorlist.append(userinput)
            check = userinput in fulldonorlist[0]
            if check:
                ind = fulldonorlist[0].index(userinput)
            else:
                fulldonorlist[0].append(userinput)
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
                if check:
                    fulldonorlist[1][ind].append(donoramount)
                else:
                    fulldonorlist[1].append([donoramount])
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
    totaldonation = []
    averagedonation = []
    numdons = []
    for i in range(0, len(fulldonorlist[0])):
        totaldonation.append(sum(int(j) for j in fulldonorlist[1][i]))
        averagedonation.append(totaldonation[i] / len(fulldonorlist[1][i]))
        numdons.append(len(fulldonorlist[1][i]))
        fulldonorlist[1][i] = sum(int(j) for j in fulldonorlist[1][i])
        fulldonorlist[2].append(averagedonation[i])

    print(fulldonorlist)
    names = fulldonorlist[0]
    sortdon = sorted(totaldonation)
    print(sortdon)

    sortedlist = fulldonorlist  # somehow magically sort the data
    print('Name         | Total |  #  |   Average ')
    print('\n______________________________________________________')
    for i in range(0, len(sortedlist[0]) - 1):
        print(names[i], totaldonation[i], numdons[i], averagedonation[i], sep = '\t')
    # somehow magically print the data
    print('\nBill Gates           |     $100.00 |   1 |     $100.00')
    input('\nPress Enter to Continue ...')
