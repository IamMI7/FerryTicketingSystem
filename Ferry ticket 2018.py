import datetime


# 1.Main menu
def menu():
    print(" -----------------------------------")
    print("            WELCOME !!!             ")
    print(" -----------------------------------")
    print(" Welcome to the ferry ticket system!!")
    print(" P - to Purchase Ticket")
    print(" V - to View seating Arrangement")
    print(" Q - to Quit the system")
    flag = str(input(" Please insert a letter for your selection: "))
    return flag


# 2. Select either BUSINESS class or ECONOMY CLASS
def purchase():
    print(" ----------------------------------------")
    print("               CLASSES                   ")
    print(" ----------------------------------------")
    print(" Welcome to the purchasing Module")
    print(" B - to Purchase ticket for BUSINESS CLASS")
    print(" E - to Purchase ticket for ECONOMY CLASS")
    print(" M - return to main menu")


def destination():
    print(" -----------------------------------")
    print("            DESTINATION             ")
    print(" -----------------------------------")
    print(" Please select your destination: ")
    print(" L-Langkawi")
    print(" P-Penang")

# Asign number relate to time and ferryID
def ferryidPtoL():
    if no == 1:
        ferryid = "001"
        time = "10.00 am"
    elif no == 2:
        ferryid = "002"
        time = "11.00 am"
    elif no == 3:
        ferryid = "003"
        time = "12.00 pm"
    elif no == 4:
        ferryid = "004"
        time = "01.00 pm"
    elif no == 5:
        ferryid = "005"
        time = "02.00 pm"
    elif no == 6:
        ferryid = "006"
        time = "03.00 pm"
    elif no == 7:
        ferryid = "007"
        time = "04.00 pm"
    else:
        ferryid = "008"
        time = "05.00 pm"
    return ferryid, time


def ferryidLtoP():
    if no == 1:
        ferryid = "005"
        time = "10.00 am"
    elif no == 2:
        ferryid = "006"
        time = "11.00 am"
    elif no == 3:
        ferryid = "007"
        time = "12.00 pm"
    elif no == 4:
        ferryid = "008"
        time = "01.00 pm"
    elif no == 5:
        ferryid = "001"
        time = "02.00 pm"
    elif no == 6:
        ferryid = "002"
        time = "03.00 pm"
    elif no == 7:
        ferryid = "003"
        time = "04.00 pm"
    else:
        ferryid = "004"
        time = "05.00 pm"
    return ferryid, time


def printseat_penangtolangkawi():
    print("---------------------------------------------------")
    print(".                PENANG TO LANGKAWI                ")
    print("---------------------------------------------------")
    print("     No.   FerryID         Time departure          ")
    print(".    1       001     ..        10.00 am      ..    ")
    print(".    2       002     ..        11.00 am      ..    ")
    print(".    3       003     ..        12.00 pm      ..    ")
    print(".    4       004     ..        01.00 pm      ..    ")
    print(".    5       005     ..        02.00 pm      ..    ")
    print(".    6       006     ..        03.00 pm      ..    ")
    print(".    7       007     ..        04.00 pm      ..    ")
    print(".    8       008     ..        04.00 pm      ..    ")


def printseat_langkawitopenang():
    print("---------------------------------------------------")
    print(".                 LANGKAWI TO PENANG               ")
    print("---------------------------------------------------")
    print("     No.   FerryID         Time departure          ")
    print(".    1       005     ..        10.00 am      ..    ")
    print(".    2       006     ..        11.00 am      ..    ")
    print(".    3       007     ..        12.00 pm      ..    ")
    print(".    4       008     ..        01.00 pm      ..    ")
    print(".    5       001     ..        02.00 pm      ..    ")
    print(".    6       002     ..        03.00 pm      ..    ")
    print(".    7       003     ..        04.00 pm      ..    ")
    print(".    8       004     ..        04.00 pm      ..    ")


def printsystem(bclass, eclass):
    print("*************************************************************")
    print("*    FerryID: 001                          Date:", datetime.date.today(), "*")
    print("*************************************************************")
    print("*    BUSINESS CLASS                                         *")
    for row in range(0, 2):
        print("*************************************************************")
        lah = ""
        for col in range(0, 5):
            lah = lah + "*" + "     " + str(bclass[row][col]) + "     "
        lah += "*"
        print (lah)
    print("*************************************************************")
    print("*    ECONOMY CLASS                                          *")
    for row in range(0, 8):
        print("*************************************************************")
        lah = ""
        for col in range(0, 5):
            lah = lah + "*" + "     " + str(eclass[row][col]) + "     "
        lah += "*"
        print (lah)
    print("*************************************************************")


# Print boarding ticket
def boardingticket(name, seatno, classes, time, destination1):
    print("------------------------------------------------------")
    print(".                BOARDING TICKET                     .")
    print("------------------------------------------------------")
    print("")
    print(".. Names:  ", name)
    print(".. Seat number:", seatno)
    print(".. Type of class: ", classes)
    print(".. Date: ", datetime.date.today())
    print(".. Time of departure: ", time)
    print(".. Destination: ", destination1)
    print("")
    print("..  ** Thanks you for choosing our company.")
    print("..        Enjoy your ride and enjoy your life. ^_^ ** ")


# assign seat number to boarding ticket.
def ticketseatno(selection, row, col):
    if selection == "b" or selection == "B":
        if row == 1:
            if col == 1:
                seatno = "1"
            elif col == 2:
                seatno = "2"
            elif col == 3:
                seatno = "3"
            elif col == 4:
                seatno = "4"
            elif col == 5:
                seatno = "5"
        if row == 2:
            if col == 1:
                seatno = "6"
            elif col == 2:
                seatno = "7"
            elif col == 3:
                seatno = "8"
            elif col == 4:
                seatno = "9"
            elif col == 5:
                seatno = "10"

    if selection == "e" or selection == "E":
        if row == 1:
            if col == 1:
                seatno = "11"
            elif col == 2:
                seatno = "12"
            elif col == 3:
                seatno = "13"
            elif col == 4:
                seatno = "14"
            elif col == 5:
                seatno = "15"
        if row == 2:
            if col == 1:
                seatno = "16"
            elif col == 2:
                seatno = "17"
            elif col == 3:
                seatno = "18"
            elif col == 4:
                seatno = "19"
            elif col == 5:
                seatno = "20"
        if row == 3:
            if col == 1:
                seatno = "21"
            elif col == 2:
                seatno = "22"
            elif col == 3:
                seatno = "23"
            elif col == 4:
                seatno = "24"
            elif col == 5:
                seatno = "25"
        if row == 4:
            if col == 1:
                seatno = "26"
            elif col == 2:
                seatno = "27"
            elif col == 3:
                seatno = "28"
            elif col == 4:
                seatno = "29"
            elif col == 5:
                seatno = "30"
        if row == 5:
            if col == 1:
                seatno = "31"
            elif col == 2:
                seatno = "32"
            elif col == 3:
                seatno = "33"
            elif col == 4:
                seatno = "34"
            elif col == 5:
                seatno = "35"
        if row == 6:
            if col == 1:
                seatno = "36"
            elif col == 2:
                seatno = "37"
            elif col == 3:
                seatno = "38"
            elif col == 4:
                seatno = "39"
            elif col == 5:
                seatno = "40"
        if row == 7:
            if col == 1:
                seatno = "41"
            elif col == 2:
                seatno = "42"
            elif col == 3:
                seatno = "43"
            elif col == 4:
                seatno = "44"
            elif col == 5:
                seatno = "45"
        if row == 8:
            if col == 1:
                seatno = "46"
            elif col == 2:
                seatno = "47"
            elif col == 3:
                seatno = "48"
            elif col == 4:
                seatno = "49"
            elif col == 5:
                seatno = "50"
    return seatno


bclassseat1 = []
for row in range(0, 2):
    bclassseat1.append([0, 0, 0, 0, 0])

eclassseat1 = []
for row in range(0, 8):
    eclassseat1.append([0, 0, 0, 0, 0])

bclassseat2 = []
for row in range(0, 2):
    bclassseat2.append([0, 0, 0, 0, 0])

eclassseat2 = []
for row in range(0, 8):
    eclassseat2.append([0, 0, 0, 0, 0])

bclassseat3 = []
for row in range(0, 2):
    bclassseat3.append([0, 0, 0, 0, 0])

eclassseat3 = []
for row in range(0, 8):
    eclassseat3.append([0, 0, 0, 0, 0])

bclassseat4 = []
for row in range(0, 2):
    bclassseat4.append([0, 0, 0, 0, 0])

eclassseat4 = []
for row in range(0, 8):
    eclassseat4.append([0, 0, 0, 0, 0])

bclassseat5 = []
for row in range(0, 2):
    bclassseat5.append([0, 0, 0, 0, 0])

eclassseat5 = []
for row in range(0, 8):
    eclassseat5.append([0, 0, 0, 0, 0])

bclassseat6 = []
for row in range(0, 2):
    bclassseat6.append([0, 0, 0, 0, 0])

eclassseat6 = []
for row in range(0, 8):
    eclassseat6.append([0, 0, 0, 0, 0])

bclassseat7 = []
for row in range(0, 2):
    bclassseat7.append([0, 0, 0, 0, 0])

eclassseat7 = []
for row in range(0, 8):
    eclassseat7.append([0, 0, 0, 0, 0])

bclassseat8 = []
for row in range(0, 2):
    bclassseat8.append([0, 0, 0, 0, 0])

eclassseat8 = []
for row in range(0, 8):
    eclassseat8.append([0, 0, 0, 0, 0])

seatno = 0
while True:
    while True:
        flag=menu()
        if flag == "p" or flag == "P":
            break
        elif flag == "v" or flag == "V":
            break
        elif flag == "q" or flag == "Q":
            break
        else:
            print(" Please try again.")

    if flag == "p" or flag == "P":
        destination()
        while True:
            leon=str(input("Pls select an option P or L:"))
            if leon == "p" or leon == "P":
                break
            elif leon == "l" or leon == "L":
                break
            else:
                print(" Please try again.")
        purchase()
        while True:
            selection = str(input(" Please insert a letter for your class seat: "))
            if selection == "B" or selection == "b":
                break
            elif selection == "E" or selection == "e":
                break
            else:
                print(" Please try again.")

        if selection == "B" or selection == "b":
            classes = "Business class"
            if leon == "p" or leon == "P":
                destination1 = " Langkawi to Penang "
                print(".....................................")
                print(".    SEATING ARRANGEMENT MODULE     .")
                print(".....................................")
                print("     F- to select Ferry ID           ")
                print("     T- to select Trip Time          ")
                while True:
                    select = str(input(" Please press F or T: "))
                    if select == "f" or select == "F":
                        break
                    elif select == "t" or select == "T":
                        break
                    else:
                        print(" Try again")
                if select == "f" or select == "F":
                    printseat_langkawitopenang()
                    no = int(input(" Please insert a number from 1 to 8: "))
                    ferryid, time = ferryidLtoP()
                elif select == "t" or select == "T":
                    printseat_langkawitopenang()
                    no = int(input(" Please insert a number from 1 to 8: "))
                    ferryid, time = ferryidLtoP()
                else:
                    print(" Sorry,invalid input.")
            elif leon == "l" or leon == "L":
                destination1 = " Penang to Langkawi "
                print(".....................................")
                print(".    SEATING ARRANGEMENT MODULE     .")
                print(".....................................")
                print("     F- to select Ferry ID           ")
                print("     T- to select Trip Time          ")
                while True:
                    select = str(input("Please press F or T: "))
                    if select == "f" or select == "F":
                        break
                    elif select == "t" or select == "T":
                        break
                    else:
                        print(" Please try again")
                if select == "f" or select == "F":
                    printseat_penangtolangkawi()
                    no = int(input(" Please insert a number from 1 to 8: "))
                    ferryid, time = ferryidPtoL()
                elif select == "t" or select == "T":
                    printseat_penangtolangkawi()
                    no = int(input(" Please insert a number from 1 to 8: "))
                    ferryid, time = ferryidPtoL()
                else:
                    print(" Sorry,invalid input.")

        elif selection == "E" or selection == "e":
            classes = "Economic class"
            if leon == "p" or leon == "P":
                destination1 = " Langkawi to Penang "
                print(".....................................")
                print(".    SEATING ARRANGEMENT MODULE     .")
                print(".....................................")
                print("     F- to select Ferry ID           ")
                print("     T- to select Trip Time          ")
                select = str(input("Please press F or T: "))
                if select == "f" or select == "F":
                    printseat_langkawitopenang()
                    no = int(input(" Please insert a number from 1 to 8: "))
                    ferryid, time = ferryidLtoP()
                elif select == "t" or select == "T":
                    printseat_langkawitopenang()
                    no = int(input(" Please insert a number from 1 to 8: "))
                    ferryid, time = ferryidLtoP()
                else:
                    print(" Sorry,invalid input.")
            elif leon == "l" or leon == "L":
                destination1 = " Penang to Langkawi "
                print(".....................................")
                print(".    SEATING ARRANGEMENT MODULE     .")
                print(".....................................")
                print("     F- to select Ferry ID           ")
                print("     T- to select Trip Time          ")
                while True:
                    select = str(input(" Please press F or T: "))
                    if select == "f" or select == "F":
                        break
                    elif select == "t" or select == "T":
                        break
                    else:
                        print(" Try again")
                if select == "f" or select == "F":
                    printseat_penangtolangkawi()
                    no = int(input(" Please insert a number from 1 to 8: "))
                    ferryid, time = ferryidPtoL()
                elif select == "t" or select == "T":
                    printseat_penangtolangkawi()
                    no = int(input(" Please insert a number from 1 to 8: "))
                    ferryid, time = ferryidPtoL()
                else:
                    print(" Sorry,invalid input.")
        elif selection == "M" or selection == "m":
            continue
        else:
            print(" Sorry,invalid input.")
    elif flag == "V" or flag == "v":
        print(".....................................")
        print(".    SEATING ARRANGEMENT MODULE     .")
        print(".....................................")
        print("     F- to select Ferry ID           ")
        print("     T- to select Trip Time          ")
        while True:
            select = str(input(" Please press F or T: "))
            if select == "f" or select == "F":
                break
            elif select == "t" or select == "T":
                break
            else:
                print(" Try again")

        destination()
        kai = str(input(" Please insert a letter for your destination: "))
        if kai == "l" or kai == "L":
            destination1 = "Penang to Langkawi "
            if select == "f" or select == "F":
                printseat_penangtolangkawi()
                no = int(input(" Please insert a number from 1 to 8: "))
                ferryid, time = ferryidPtoL()
                purchase()
                selection = str(input(" Please insert a letter for your class seat: "))
                if selection == "b" or selection == "B":
                    classes = "b"
                elif selection == "e" or selection == "E":
                    classes = "e"
                else:
                    print (" Sorry,invalid input.")
            elif select == "t" or select == "T":
                printseat_penangtolangkawi()
                no = int(input(" Please insert a number from 1 to 8: "))
                ferryid, time = ferryidPtoL()
                purchase()
                selection = str(input(" Please insert a letter for your class seat: "))
                if selection == "b" or selection == "B":
                    classes = "b"
                elif selection == "e" or selection == "E":
                    classes = "e"
                else:
                    print (" Sorry,invalid input.")
            else:
                print(" Sorry,invalid input.")
        elif kai == "p" or kai == "P":
            destination1 = "Langkawi to Penang "
            if select == "f" or select == "F":
                printseat_langkawitopenang()
                no = int(input(" Please insert a number from 1 to 8: "))
                ferryid, time = ferryidLtoP()
                purchase()
                selection = str(input(" Please insert a letter for your class seat: "))
                if selection == "b" or selection == "B":
                    classes = "b"
                elif selection == "e" or selection == "E":
                    classes = "e"
                else:
                    print (" Sorry,invalid input.")
            elif select == "t" or select == "T":
                printseat_langkawitopenang()
                no = int(input(" Please insert a number from 1 to 8: "))
                ferryid, time = ferryidLtoP()
                purchase()
                selection = str(input(" Please insert a letter for your class seat: "))
                if selection == "b" or selection == "B":
                    classes = "b"
                elif selection == "e" or selection == "E":
                    classes = "e"
                else:
                    print (" Sorry,invalid input.")
            else:
                print(" Sorry,invalid input.")

    if selection == "b" or selection == "B":
        print(".............................")
        print("       Business class        ")
        print(".............................")
        if no == 1:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 2):
                lol = bclassseat1[i]
                print(lol)
            row = int(input(" Please enter a value from 1-2 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 2 and row >= 1) and (col <= 5 and col >= 1):
                if bclassseat1[row - 1][col - 1] == 0:
                    bclassseat1[row - 1][col - 1] = 1
                    printsystem(bclassseat1, eclassseat1)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")
            break

            if not bclassseat1 in [0]:
                print (" All business class seat are fully booked.")
                print (" Please proceed to the next trip, press A or book the economic class seats, press B. ")
                selection = str(input(" Enter a selection: "))
                if selection == "A" or selection == "a":
                    print(" Next business class trip leaves in 1 hour, please return to main menu.")
                    menu()
                    flag = str(input(" Please insert a letter for your selection: "))
                elif selection == "B" or selection == "b":
                    for i in range(0, 8):
                        bclassfull = eclassseat1[i]
                        print(bclassfull)
                    row = int(input(" Please enter a value from 1-8 for row: "))
                    col = int(input(" Please enter a value from 1-5 for column: "))
                    seatno = ticketseatno(selection, row, col)
                    if eclassseat1[row - 1][col - 1] == 0:
                        eclassseat1[row - 1][col - 1] = 1
                        printsystem(bclassseat1, eclassseat1)
                        boardingticket(name, seatno, classes, time, destination1)
                        userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                        if (userinput == 1):
                            continue
                        elif (userinput == 2):
                            break
                        else:
                            print("invalid input")
                    else:
                        print(" Sorry,the seat had been booked.")


        elif no == 2:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 2):
                lol = bclassseat2[i]
                print(lol)
            row = int(input(" Please enter a value from 1-2 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 2 and row >= 1) and (col <= 5 and col >= 1):
                if bclassseat2[row - 1][col - 1] == 0:
                    bclassseat2[row - 1][col - 1] = 1
                    printsystem(bclassseat2, eclassseat2)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")
            break

            if not bclassseat2 in [0]:
                print (" All business class seat are fully booked.")
                print (" Please proceed to the next trip, press A or book the economic class seats, press B. ")
                selection = str(input(" Enter a selection: "))
                if selection == "A" or selection == "a":
                    print(" Next business class trip leaves in 1 hour")
                    menu()
                    flag = str(input(" Please insert a letter for your selection: "))
                elif selection == "B" or selection == "b":
                    for i in range(0, 8):
                        bclassfull = eclassseat2[i]
                        print(bclassfull)
                    row = int(input(" Please enter a value from 1-8 for row: "))
                    col = int(input(" Please enter a value from 1-5 for column: "))
                    seatno = ticketseatno(selection, row, col)
                    if eclassseat2[row - 1][col - 1] == 0:
                        eclassseat2[row - 1][col - 1] = 1
                        printsystem(bclassseat2, eclassseat2)
                        boardingticket(name, seatno, classes, time, destination1)
                        userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                        if (userinput == 1):
                            continue
                        elif (userinput == 2):
                            break
                        else:
                            print("invalid input")
                    else:
                        print(" Sorry,the seat had been booked.")
        elif no == 3:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 2):
                lol = bclassseat3[i]
                print(lol)
            row = int(input(" Please enter a value from 1-2 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 2 and row >= 1) and (col <= 5 and col >= 1):
                if bclassseat3[row - 1][col - 1] == 0:
                    bclassseat3[row - 1][col - 1] = 1
                    printsystem(bclassseat3, eclassseat3)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")
            break

            if not bclassseat3 in [0]:
                print (" All business class seat are fully booked.")
                print (" Please proceed to the next trip, press A or book the economic class seats, press B. ")
                selection = str(input(" Enter a selection: "))
                if selection == "A" or selection == "a":
                    print(" Next business class trip leaves in 1 hour")
                    menu()
                    flag = str(input(" Please insert a letter for your selection: "))
                elif selection == "B" or selection == "b":
                    for i in range(0, 8):
                        bclassfull = eclassseat3[i]
                        print(bclassfull)
                    row = int(input(" Please enter a value from 1-8 for row: "))
                    col = int(input(" Please enter a value from 1-5 for column: "))
                    seatno = ticketseatno(selection, row, col)
                    if eclassseat3[row - 1][col - 1] == 0:
                        eclassseat3[row - 1][col - 1] = 1
                        printsystem(bclassseat3, eclassseat3)
                        boardingticket(name, seatno, classes, time, destination1)
                        userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                        if (userinput == 1):
                            continue
                        elif (userinput == 2):
                            break
                        else:
                            print("invalid input")
                    else:
                        print(" Sorry,the seat had been booked.")
        elif no == 4:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 2):
                lol = bclassseat4[i]
                print(lol)
            row = int(input(" Please enter a value from 1-2 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 2 and row >= 1) and (col <= 5 and col >= 1):
                if bclassseat4[row - 1][col - 1] == 0:
                    bclassseat4[row - 1][col - 1] = 1
                    printsystem(bclassseat4, eclassseat4)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")
            break

            if not bclassseat4 in [0]:
                print (" Sorry,all business class seats are fully booked.")
                print (" Please proceed to the next trip, press A or book the economic class seats, press B. ")
                selection = str(input(" Enter a selection: "))
                if selection == "A" or selection == "a":
                    print(" Next business class trip leaves in 1 hour")
                    menu()
                    flag = str(input(" Please insert a letter for your selection: "))
                elif selection == "B" or selection == "b":
                    for i in range(0, 8):
                        bclassfull = eclassseat4[i]
                        print(bclassfull)
                    row = int(input(" Please enter a value from 1-8 for row: "))
                    col = int(input(" Please enter a value from 1-5 for column: "))
                    seatno = ticketseatno(selection, row, col)
                    if eclassseat4[row - 1][col - 1] == 0:
                        eclassseat4[row - 1][col - 1] = 1
                        printsystem(bclassseat4, eclassseat4)
                        boardingticket(name, seatno, classes, time, destination1)
                        userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                        if (userinput == 1):
                            continue
                        elif (userinput == 2):
                            break
                        else:
                            print("invalid input")
                    else:
                        print(" Sorry,the seat had been booked.")

        elif no == 5:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 2):
                lol = bclassseat5[i]
                print(lol)
            row = int(input(" Please enter a value from 1-2 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 2 and row >= 1) and (col <= 5 and col >= 1):
                if bclassseat5[row - 1][col - 1] == 0:
                    bclassseat5[row - 1][col - 1] = 1
                    printsystem(bclassseat5, eclassseat5)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")

            if not bclassseat5 in [0]:
                print (" All business class seat are fully booked.")
                print (" Please proceed to the next trip, press A or book the economic class seats, press B. ")
                selection = str(input(" Enter a selection: "))
                if selection == "A" or selection == "a":
                    print(" Next business class trip leaves in 1 hour")
                    menu()
                    flag = str(input(" Please insert a letter for your selection: "))
                elif selection == "B" or selection == "b":
                    for i in range(0, 8):
                        bclassfull = eclassseat5[i]
                        print(bclassfull)
                    row = int(input(" Please enter a value from 1-8 for row: "))
                    col = int(input(" Please enter a value from 1-5 for column: "))
                    seatno = ticketseatno(selection, row, col)
                    if eclassseat5[row - 1][col - 1] == 0:
                        eclassseat5[row - 1][col - 1] = 1
                        printsystem(bclassseat5, eclassseat5)
                        boardingticket(name, seatno, classes, time, destination1)
                        userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                        if (userinput == 1):
                            continue
                        elif (userinput == 2):
                            break
                        else:
                            print("invalid input")
                    else:
                        print(" Sorry,the seat had been booked.")
        elif no == 6:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 2):
                lol = bclassseat6[i]
                print(lol)
            row = int(input(" Please enter a value from 1-2 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 2 and row >= 1) and (col <= 5 and col >= 1):
                if bclassseat6[row - 1][col - 1] == 0:
                    bclassseat6[row - 1][col - 1] = 1
                    printsystem(bclassseat6, eclassseat6)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")
            break

            if not bclassseat6 in [0]:
                print (" All business class seat are fully booked.")
                print (" Please proceed to the next trip, press A or book the economic class seats, press B. ")
                selection = str(input(" Enter a selection: "))
                if selection == "A" or selection == "a":
                    print(" Next business class trip leaves in 1 hour")
                    menu()
                    flag = str(input(" Please insert a letter for your selection: "))
                elif selection == "B" or selection == "b":
                    for i in range(0, 8):
                        bclassfull = eclassseat6[i]
                        print(bclassfull)
                    row = int(input(" Please enter a value from 1-8 for row: "))
                    col = int(input(" Please enter a value from 1-5 for column: "))
                    seatno = ticketseatno(selection, row, col)
                    if eclassseat6[row - 1][col - 1] == 0:
                        eclassseat6[row - 1][col - 1] = 1
                        printsystem(bclassseat6, eclassseat6)
                        boardingticket(name, seatno, classes, time, destination1)
                        userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                        if (userinput == 1):
                            continue
                        elif (userinput == 2):
                            break
                        else:
                            print("invalid input")
                    else:
                        print(" Sorry,the seat had been booked.")
        elif no == 7:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 2):
                lol = bclassseat7[i]
                print(lol)
            row = int(input(" Please enter a value from 1-2 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 2 and row >= 1) and (col <= 5 and col >= 1):
                if bclassseat7[row - 1][col - 1] == 0:
                    bclassseat7[row - 1][col - 1] = 1
                    printsystem(bclassseat7, eclassseat7)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")
            break

            if not bclassseat7 in [0]:
                print (" All business class seat are fully booked.")
                print (" Please proceed to the next trip, press A or book the economic class seats, press B. ")
                selection = str(input(" Enter a selection: "))
                if selection == "A" or selection == "a":
                    print(" Next business class trip leaves in 1 hour")
                    menu()
                    flag = str(input(" Please insert a letter for your selection: "))
                elif selection == "B" or selection == "b":
                    for i in range(0, 8):
                        bclassfull = eclassseat7[i]
                        print(bclassfull)
                    row = int(input(" Please enter a value from 1-8 for row: "))
                    col = int(input(" Please enter a value from 1-5 for column: "))
                    seatno = ticketseatno(selection, row, col)
                    if eclassseat7[row - 1][col - 1] == 0:
                        eclassseat7[row - 1][col - 1] = 1
                        printsystem(bclassseat7, eclassseat7)
                        boardingticket(name, seatno, classes, time, destination1)
                        userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                        if (userinput == 1):
                            continue
                        elif (userinput == 2):
                            break
                        else:
                            print("invalid input")
                    else:
                        print(" Sorry,the seat had been booked.")
        elif no == 8:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 2):
                lol = bclassseat8[i]
                print(lol)
            row = int(input(" Please enter a value from 1-2 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 2 and row >= 1) and (col <= 5 and col >= 1):
                if bclassseat8[row - 1][col - 1] == 0:
                    bclassseat8[row - 1][col - 1] = 1
                    printsystem(bclassseat8, eclassseat8)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")

            if not bclassseat8 in [0]:
                print (" All business class seat are fully booked.")
                print (" Please proceed to the next trip, press A or book the economic class seats, press B. ")
                selection = str(input(" Enter a selection: "))
                if selection == "A" or selection == "a":
                    print(" Next business class trip leaves in 1 hour")
                    menu()
                    flag = str(input(" Please insert a letter for your selection: "))
                elif selection == "B" or selection == "b":
                    for i in range(0, 8):
                        bclassfull = eclassseat8[i]
                        print(bclassfull)
                    row = int(input(" Please enter a value from 1-8 for row: "))
                    col = int(input(" Please enter a value from 1-5 for column: "))
                    seatno = ticketseatno(selection, row, col)
                    if eclassseat8[row - 1][col - 1] == 0:
                        eclassseat8[row - 1][col - 1] = 1
                        printsystem(bclassseat8, eclassseat8)
                        boardingticket(name, seatno, classes, time, destination1)
                        userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                        if (userinput == 1):
                            continue
                        elif (userinput == 2):
                            break
                        else:
                            print("invalid input")
                    else:
                        print(" Sorry,the seat had been booked.")
    elif selection == "e" or selection == "E":
        print(".............................")
        print("       Economic class        ")
        print(".............................")
        if no == 1:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 8):
                lol = eclassseat1[i]
                print(lol)
            row = int(input(" Please enter a value from 1-8 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 8 and row >= 1) and (col <= 5 and col >= 1):
                if eclassseat1[row - 1][col - 1] == 0:
                    eclassseat1[row - 1][col - 1] = 1
                    printsystem(bclassseat1, eclassseat1)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")

        elif no == 2:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 8):
                lol = eclassseat2[i]
                print(lol)
            row = int(input(" Please enter a value from 1-8 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 8 and row >= 1) and (col <= 5 and col >= 1):
                if eclassseat2[row - 1][col - 1] == 0:
                    eclassseat2[row - 1][col - 1] = 1
                    printsystem(bclassseat2, eclassseat2)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")

        elif no == 3:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 8):
                lol = eclassseat3[i]
                print(lol)
            row = int(input(" Please enter a value from 1-8 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 8 and row >= 1) and (col <= 5 and col >= 1):
                if eclassseat3[row - 1][col - 1] == 0:
                    eclassseat3[row - 1][col - 1] = 1
                    printsystem(bclassseat3, eclassseat3)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")

        elif no == 4:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 8):
                lol = eclassseat4[i]
                print(lol)
            row = int(input(" Please enter a value from 1-8 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 8 and row >= 1) and (col <= 5 and col >= 1):
                if eclassseat4[row - 1][col - 1] == 0:
                    eclassseat4[row - 1][col - 1] = 1
                    printsystem(bclassseat4, eclassseat4)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")

        elif no == 5:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 8):
                lol = eclassseat5[i]
                print(lol)
            row = int(input(" Please enter a value from 1-8 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 8 and row >= 1) and (col <= 5 and col >= 1):
                if eclassseat5[row - 1][col - 1] == 0:
                    eclassseat5[row - 1][col - 1] = 1
                    printsystem(bclassseat5, eclassseat5)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")

        elif no == 6:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 8):
                lol = eclassseat6[i]
                print(lol)
            row = int(input(" Please enter a value from 1-8 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 8 and row >= 1) and (col <= 5 and col >= 1):
                if eclassseat6[row - 1][col - 1] == 0:
                    eclassseat6[row - 1][col - 1] = 1
                    printsystem(bclassseat6, eclassseat6)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")

        elif no == 7:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 8):
                lol = eclassseat7[i]
                print(lol)
            row = int(input(" Please enter a value from 1-8 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 8 and row >= 1) and (col <= 5 and col >= 1):
                if eclassseat7[row - 1][col - 1] == 0:
                    eclassseat7[row - 1][col - 1] = 1
                    printsystem(bclassseat7, eclassseat7)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")
        elif no == 8:
            name = str(input(" Please insert your names as per IC: "))
            for i in range(0, 8):
                lol = eclassseat8[i]
                print(lol)
            row = int(input(" Please enter a value from 1-8 for row: "))
            col = int(input(" Please enter a value from 1-5 for column: "))
            seatno = ticketseatno(selection, row, col)
            if (row <= 8 and row >= 1) and (col <= 5 and col >= 1):
                if eclassseat8[row - 1][col - 1] == 0:
                    eclassseat8[row - 1][col - 1] = 1
                    printsystem(bclassseat8, eclassseat8)
                    boardingticket(name, seatno, classes, time, destination1)
                    userinput = int(input("press 1 to return to main menu \npress 2 to exit program: "))
                    if (userinput == 1):
                        continue
                    elif (userinput == 2):
                        break
                    else:
                        print("invalid input")
                else:
                    print(" Sorry,the seat had been booked.")
            else:
                print(" Invalid input.")
        else:
            print(" Sorry,invalid input")

























