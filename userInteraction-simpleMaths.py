# Author's name:            Lukas Mohs
# Creation Date:            03/23/17
# Last Modification Date:   03/23/17
# Brief Description:
# This program takes a speed in miles per hour as user input and offers
# four options to convert it to different units. After completion, the user can perform
# another calculation
import getpass
print("Hello", getpass.getuser(), "! Welcome to this small calculation program")
repeat = "y"
while repeat == "y":
    mph = float(input("Please enter a floating point value specifying miles per hour:"))
    print("Thanks for your input: ", mph)
    print("Now, please select how you want to convert your input:")
    print("1. Barleycorns/day")
    print("2. Furlongs/fortnight")
    print("3. Mach number")
    print("4. Percentage of the speed of light")
    selection = input("your selection:");
    if selection == "1":
        milesPerDay = mph * 24
        metersPerDay = milesPerDay * 1609
        bcd = metersPerDay *  117
        print(mph," miles/hour are ", bcd, " Barleycorns/day")
    elif selection == "2":
        yardsPerHour = mph * 1760
        furlongsPerHour = yardsPerHour / 220
        flfn = furlongsPerHour * 336
        print(mph," miles/hour are ", flfn, " Furlongs/fortnight")
    elif selection == "3":
        mach = mph * 0.00130332
        print(mph," miles/hour are ", mach, " Mach")
    elif selection == "4":
        percentageOfSpeedOfLight = (mph*0.44704)  / 299792458
        print(mph," miles/hour are ", percentageOfSpeedOfLight, " % of the speed of light")
    repeat = input("\nDo you want to perform another calculation (y/n)?");
