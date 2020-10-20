User = input('Hello! Would you please tell your name?: ')
print('Good day, Sir/Maam'+ User +'!')
import os
R = 0.0821 #Ideal Gas Constant in L*atm/mol*k
def converter(Pressure): #Conversion of all Pressure Values into Atmospheric units (atm)
    atm = Pressure.find('atm')
    KPa = Pressure.find('KPa')
    mmHg = Pressure.find('mmHg')
    torr = Pressure.find('torr')
    psi = Pressure.find('psi')
    if (atm == -1) and (KPa != -1) and (mmHg == -1) and (torr == -1) and (psi == -1):
        removed_unit = Pressure[0:int(KPa)]
        converted_pressure = float(removed_unit) * 101.30
        return converted_pressure
    elif (atm == -1) and (KPa == -1) and (mmHg != -1) and (torr == -1) and (psi == -1):
        removed_unit = Pressure[0:int(mmHg)]
        converted_pressure = float(removed_unit) * 760.00
        return converted_pressure
    elif (atm == -1) and (KPa == -1) and (mmHg == -1) and (torr != -1) and (psi == -1):
        removed_unit = Pressure[0:int(torr)]
        converted_pressure = float(removed_unit) * 760.00
        return converted_pressure
    elif (atm == -1) and (KPa == -1) and (mmHg == -1) and (torr == -1) and (psi != -1):
        removed_unit = Pressure[0:int(psi)]
        converted_pressure = float(removed_unit) * 14.60
        return converted_pressure
    elif (atm != -1) and (KPa == -1) and (mmHg == -1) and (torr == -1) and (psi == -1):
        removed_unit = Pressure[0:int(atm)]
        converted_pressure = float(removed_unit)
        return converted_pressure

def converter_02(Volume): #Conversion of all Volume-related values into Liters
    Liters = Volume.find('L')
    milliliters = Volume.find('ml')
    if (Liters != -1) and (milliliters == -1):
        removed_unit = Volume[0:int(Liters)]
        converted_volume = float(removed_unit)
        return converted_volume
    elif (milliliters != -1) and (Liters == -1):
        removed_unit = Volume[0:int(milliliters)]
        converted_volume = float(removed_unit) / 1000.00
        return converted_volume
    
def converter_03(Temp): #Conversion of all Temperature values into Kelvin (K)
    Kelvin = Temp.find('K')
    Celcius = Temp.find('C')
    if (Kelvin != -1) and (Celcius == -1):
        removed_unit = Temp[0:int(Kelvin)]
        converted_temperature = float(removed_unit)
        return converted_temperature
    elif (Celcius != -1) and (Kelvin == -1):
        removed_unit = Temp[0:int(Celcius)]
        converted_temperature = float(removed_unit) + 273.00
        return converted_temperature

def converter_04(Moles): #Removal of mol units in the given Mole Value
    mol = Moles.find('mol')
    removed_unit = Moles[0:int(mol)]
    converted_mol = float(removed_unit)
    return converted_mol

def converter_05(Mass): #Here we go! HA↗HA↘HA↗HA↘HA↗HA↘HA↗HA↘HA↗HA↘
    from molmass import Formula
    formula = Formula(Mass)
    return formula.mass

def converter_06(Weight): #Conversion of all Weight and Mass related units into Grams (g)
    g = Weight.find('g')
    grams = Weight.find('grams')
    if (g != -1) and (grams == -1):
        removed_unit = Weight[0:int(g)]
        converted_unit = float(removed_unit)
        return converted_unit
    elif (grams != -1) and (g == -1):
        removed_unit = Weight[0:int(grams)]
        converted_unit = float(removed_unit)
        return converted_unit

print('What do you want for this program to find?')
print('You wil be asked later on what is given and what is Missing.')
print('This is currently a simple program ran on Command Line so It is a bit Hard')
def problem_solver(): #The main program
    print("a) Boyle's Law (P1V1 = P2V2)")
    print("b) Charles' Law (V1/T1 = V2/T2)")
    print("c) Avogadro's Law (V1/n1 = V2/n2)")
    print("d) Gay Lussac's Law (P1/T1 = P2/T2)")
    print("e) Combined Gas Law (P1V1/T1 = P2V2/T2)")
    print("f) Ideal Gas Law (PV = nRT)")
    print("g) Dalton's Partial Pressure")
    selection = input('What do you want for this program to find? ')
    if (selection == 'a') or (selection == 'A'):
        print("Boyle's Law (P1V1 = P2V2)")
        print('There are four Variables, namely Initial Pressure and Volume (P1 and V1) and Final Pressure and Volume (P2 and V2)')
        print('Please Type what Variables are Given and What is missing and same format as below:')
        print('G G G U = P1 V1 and P2 is Given, V2 is Missing or Unknown')
        print('G G U G = P1 V1 and V2 is Given, P2 is Missing or Unknown')
        print('G U G G = P1 P2 and V2 is Given, V1 is Missing or Unknown')
        print('U G G G = V1 P2 and V2 is Given, P1 is Missing or Unknown')
        BLDerive = input("Please type what are the Given and the Unknown: ")
        if (BLDerive == 'G G G U') or (BLDerive == 'GGGU') or (BLDerive =='gggu') or (BLDerive == 'g g g u'):
            P1 = input('Please type the value of the Initial Presssure along with its unit: ')
            P1_converted = converter(P1) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1) # Removal of the Unit from the given Volume data
            P2 = input('Please type the value of the Final Pressure along with its unit: ')
            P2_converted = converter(P2) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            print('Processing')
            answer = (P1_converted * V1_converted) / P2_converted
            print('The Final Volume is '+ str(answer) + ' Liters')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (BLDerive == 'G G U G') or (BLDerive == 'GGUG') or (BLDerive =='ggug') or (BLDerive == 'g g u g'):
            P1 = input('Please type the value of the Initial Presssure along with its unit: ')
            P1_converted = converter(P1) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1) # Removal of the Unit from the given Volume data
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2) # Removal of the Unit from the given Volume data
            print('Processing')
            answer = (P1_converted * V1_converted) / V2_converted
            print('The Final Pressure is '+ str(answer) + ' atm')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (BLDerive == 'G U G G') or (BLDerive == 'GUGG') or (BLDerive =='gugg') or (BLDerive == 'g u g g'):
            P1 = input('Please type the value of the Initial Presssure along with its unit: ')
            P1_converted = converter(P1) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            P2 = input('Please type the value of the Final Pressure along with its unit: ')
            P2_converted = converter(P2) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2) # Removal of the Unit from the given Volume data
            print('Processing')
            answer = (P2_converted * V2_converted) / P1_converted
            print('The Initial Volume is '+ str(answer) + ' Liters')
            os.system('pause') 
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (BLDerive == 'U G G G') or (BLDerive == 'UGGG') or (BLDerive =='uggg') or (BLDerive == 'u g g g'):
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1) # Removal of the Unit from the given Volume data
            P2 = input('Please type the value of the Final Pressure along with its unit: ')
            P2_converted = converter(P2) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2) # Removal of the Unit from the given Volume data
            print('Processing')
            answer = (P2_converted * V2_converted) / V1_converted
            print('The Initial Pressure is '+ str(answer) + ' atm')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        else:
            print('Given the choice you gave, no possible equations are available to solve it.')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
    elif (selection == 'b') or (selection == 'B'):
        print("Charles' Law (V1/T1 = V2/T2)")
        print('There are four Variables, namely Initial Volume and Temperature (V1 and T1) and Final Temperature and Volume (V2 and T2)')
        print('Please Type what Variables are Given and What is missing and same format as below:')
        print('G G G U = V1 T1 and V2 is Given, T2 is Missing or Unknown')
        print('G G U G = V1 T1 and T2 is Given, V2 is Missing or Unknown')
        print('G U G G = V1 V2 and T2 is Given, T1 is Missing or Unknown')
        print('U G G G = T1 V2 and T2 is Given, V1 is Missing or Unknown')
        CLDerive = input("Please type what are the Given and the Unknown: ")
        if (CLDerive == 'G G G U') or (CLDerive == 'GGGU') or (CLDerive =='gggu') or (CLDerive == 'g g g u'):
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1)
            T1 = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T1_converted = converter_03(T1)
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2)
            print('Processing')
            answer = (V2_converted * T1_converted) * V1_converted
            print('The Final Temperature is ' + str(answer) + ' Kelvin')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (CLDerive == 'G G U G') or (CLDerive == 'GGUG') or (CLDerive =='ggug') or (CLDerive == 'g g u g'):
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1)
            T1 = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T1_converted = converter_03(T1)
            T2 = input('Please type the value of the Final Temperature along with its unit (K or C): ')
            T2_converted = converter_03(T2)
            print('Processing')
            answer = (V1_converted * T2_converted) / T1_converted
            print('The Final Volume is ' + str(answer) + 'Liters')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (CLDerive == 'G U G G') or (CLDerive == 'GUGG') or (CLDerive =='gugg') or (CLDerive == 'g u g g'):
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1)
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2)
            T2 = input('Please type the value of the Final Temperature along with its unit (K or C): ')
            T2_converted = converter_03(T2)
            print('Processing')
            answer = (V1_converted * T2_converted) / V2_converted
            print('The Initial Temperature is ' + str(answer) + 'Kelvin')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (CLDerive == 'U G G G') or (CLDerive == 'UGGG') or (CLDerive =='uggg') or (CLDerive == 'u g g g'):
            T1 = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T1_converted = converter_03(T1)
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2)
            T2 = input('Please type the value of the Final Temperature along with its unit (K or C): ')
            T2_converted = converter_03(T2)
            print('Processing')
            answer = (V2_converted * T1_converted) / T2_converted
            print('The Initial Volume is ' + str(answer) + ' Liters')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        else:
            print('Given the choice you gave, no possible equations are available to solve it.')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
    elif (selection == 'c') or (selection == 'C'):
        print("Avogadro's Law (V1/n1 = V2/n2)")
        print('There are four Variables, namely Initial Volume and Mole Value (V1 and n1) and Final Volume and Mole Value (V2 and n2)')
        print('Please Type what Variables are Given and What is missing and same format as below:')
        print('G G G U = V1 n1 and V2 is Given, n2 is Missing or Unknown')
        print('G G U G = V1 n1 and n2 is Given, V2 is Missing or Unknown')
        print('G U G G = V1 V2 and n2 is Given, n1 is Missing or Unknown')
        print('U G G G = n1 V2 and n2 is Given, V1 is Missing or Unknown')
        ALDerive = input("Please type what are the Given and the Unknown: ")
        if (ALDerive == 'G G G U') or (ALDerive == 'GGGU') or (ALDerive =='gggu') or (ALDerive == 'g g g u'):
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1)
            n1 = input('Please type the value of the Initial Moles of Gas along with its unit (mol): ')
            n1_converted = converter_04(n1)
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2)
            print('Processing')
            answer = (V2_converted * n1_converted) / V1_converted
            print('The Final Moles of Gas is ' + str(answer) + ' mol')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (ALDerive == 'G G U G') or (ALDerive == 'GGUG') or (ALDerive =='ggug') or (ALDerive == 'g g u g'):
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1)
            n1 = input('Please type the value of the Initial Moles of Gas along with its unit (mol): ')
            n1_converted = converter_04(n1)
            n2 = input('Please type the value of the Final Moles of Gas along with its unit (mol): ')
            n2_converted = converter_04(n2)
            print('Processing')
            answer = (V1_converted * n2_converted) / n1_converted
            print('The Final Volume of Gas is ' + str(answer) + ' Liters')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (ALDerive == 'G U G G') or (ALDerive == 'GUGG') or (ALDerive =='gugg') or (ALDerive == 'g u g g'):
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1)
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2)
            n2 = input('Please type the value of the Final Moles of Gas along with its unit (mol): ')
            n2_converted = converter_04(n2)
            print('Processing')
            answer = (V1_converted * n2_converted) / V2_converted
            print('The initial Moles of Gas is ' + str(answer) + ' mol')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (ALDerive == 'U G G G') or (ALDerive == 'UGGG') or (ALDerive =='uggg') or (ALDerive == 'u g g g'):
            n1 = input('Please type the value of the Initial Moles of Gas along with its unit (mol): ')
            n1_converted = converter_04(n1)
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2)
            n2 = input('Please type the value of the Final Moles of Gas along with its unit (mol): ')
            n2_converted = converter_04(n2)
            print('Processing')
            answer = (V2_converted * n1_converted) / n2_converted
            print('The Initial Volume of Gas is ' + str(answer) + ' Liters')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        else:
            print('Given the choice you gave, no possible equations are available to solve it.')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
    elif (selection == 'd') or (selection == 'D'):
        print("Gay Lussac's Law (P1/T1 = P2/T2)")
        print('There are four Variables, namely Initial Presure and Temperature (P1 and T1) and Final Pressure and Temperature (V2 and n2)')
        print('Please Type what Variables are Given and What is missing and same format as below:')
        print('G G G U = P1 T1 and P2 is Given, T2 is Missing or Unknown')
        print('G G U G = P1 T1 and T2 is Given, P2 is Missing or Unknown')
        print('G U G G = P1 P2 and T2 is Given, T1 is Missing or Unknown')
        print('U G G G = T1 P2 and T2 is Given, P1 is Missing or Unknown')
        GLLDerive = input("Please type what are the Given and the Unknown: ")
        if (GLLDerive == 'G G G U') or (GLLDerive == 'GGGU') or (GLLDerive =='gggu') or (GLLDerive == 'g g g u'):
            P1 = input('Please type the value of the Initial Presssure along with its unit: ')
            P1_converted = converter(P1) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            T1 = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T1_converted = converter_03(T1)
            P2 = input('Please type the value of the Final Pressure along with its unit: ')
            P2_converted = converter(P2) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            print('Processing')
            answer = (P2_converted * T1_converted) / P1_converted
            print('The Final Temperature is ' + str(answer) + ' Kelvin')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (GLLDerive == 'G G U G') or (GLLDerive == 'GGUG') or (GLLDerive =='ggug') or (GLLDerive == 'g g u g'):
            P1 = input('Please type the value of the Initial Presssure along with its unit: ')
            P1_converted = converter(P1) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            T1 = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T1_converted = converter_03(T1)
            T2 = input('Please type the value of the Final Temperature along with its unit (K or C): ')
            T2_converted = converter_03(T2)
            print('Processing')
            answer = (P1_converted * T2_converted) / T1_converted
            print('The Final Pressure is ' + str(answer) + ' atm')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (GLLDerive == 'G U G G') or (GLLDerive == 'GUGG') or (GLLDerive =='gugg') or (GLLDerive == 'g u g g'):
            P1 = input('Please type the value of the Initial Presssure along with its unit: ')
            P1_converted = converter(P1) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            P2 = input('Please type the value of the Final Pressure along with its unit: ')
            P2_converted = converter(P2) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            T2 = input('Please type the value of the Final Temperature along with its unit (K or C): ')
            T2_converted = converter_03(T2)
            print('Processing')
            answer = (P1_converted * T2_converted) / P2_converted
            print('The Initial Temperature is ' + str(answer) + ' Kelvin')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (GLLDerive == 'U G G G') or (GLLDerive == 'UGGG') or (GLLDerive =='uggg') or (GLLDerive == 'u g g g'):
            T1 = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T1_converted = converter_03(T1)
            P2 = input('Please type the value of the Final Pressure along with its unit: ')
            P2_converted = converter(P2) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            T2 = input('Please type the value of the Final Temperature along with its unit (K or C): ')
            T2_converted = converter_03(T2)
            print('Processing')
            answer = (P2_converted * T1_converted) / T2_converted
            print('The Initial Pressure is ' + str(answer) + ' atm')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        else:
            print('Given the choice you gave, no possible equations are available to solve it.')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
    elif (selection == 'e') or (selection == 'E'):
        print("Combined Gas Law (P1V1/T1 = P2V2/T2)")
        print('There are six Variables, namely Initial Pressure, Volume, Temperature (P1, V1, and T1), \nand Final Pressure, Volume, and Temperature (P2, V2, and T2)')
        print('Please Type what Variables are Given and What is missing and same format as below:')
        print('G G G G G U = P1 V1 T1 P2 and V2 is Given, T2 is Missing or Unknown')
        print('G G G G U G = P1 V1 T1 P2 and T2 is Given, V2 is Missing or Unknown')
        print('G G G U G G = P1 V1 T1 V2 and T2 is Given, P2 is Missing or Unknown')
        print('G G U G G G = P1 V1 P2 V2 and T2 is Given, T1 is Missing or Unknown')
        print('G U G G G G = P1 T1 P2 V2 and T2 is Given, V1 is Missing or Unknown')
        print('U G G G G G = V1 T1 P2 V2 and T2 is Given, P1 is Missing or Unknown')
        CGLDerive = input("Please type what are the Given and the Unknown: ")
        if (CGLDerive.upper() == 'G G G G G U') or (CGLDerive.upper() == 'GGGGGU'):
            P1 = input('Please type the value of the Initial Presssure along with its unit: ')
            P1_converted = converter(P1) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1)
            T1 = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T1_converted = converter_03(T1)
            P2 = input('Please type the value of the Final Pressure along with its unit: ')
            P2_converted = converter(P2) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2)
            print('Processing')
            answer = (P2_converted * V2_converted * T1_converted) / (P1_converted * V1_converted)
            print('The Final Temperature is ' + str(answer) + ' Kelvin')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (CGLDerive.upper() == 'G G G G U G') or (CGLDerive.upper() == 'GGGGUG'):
            P1 = input('Please type the value of the Initial Presssure along with its unit: ')
            P1_converted = converter(P1) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1)
            T1 = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T1_converted = converter_03(T1)
            P2 = input('Please type the value of the Final Pressure along with its unit: ')
            P2_converted = converter(P2) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            T2 = input('Please type the value of the Final Temperature along with its unit (K or C): ')
            T2_converted = converter_03(T2)
            print('Processing')
            answer = (P1_converted * V1_converted * T2_converted) / (T1_converted * P2_converted)
            print('The final Volume is ' + str(answer) + ' Liters')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (CGLDerive.upper() == 'G G G U G G') or (CGLDerive.upper() == 'GGGUGG'):
            P1 = input('Please type the value of the Initial Presssure along with its unit: ')
            P1_converted = converter(P1) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1)
            T1 = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T1_converted = converter_03(T1)
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2)
            T2 = input('Please type the value of the Final Temperature along with its unit (K or C): ')
            T2_converted = converter_03(T2)
            print('Processing')
            answer = (P1_converted * V1_converted * T2_converted) / (T1_converted * P2_converted)
            print('The Final Pressure is ' + str(answer) + ' atm')
            os.system('pause')
            os.system('cls')
        elif (CGLDerive.upper() == 'G G U G G G') or (CGLDerive.upper() == 'GGUGGG'):
            P1 = input('Please type the value of the Initial Presssure along with its unit: ')
            P1_converted = converter(P1) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1)
            P2 = input('Please type the value of the Final Pressure along with its unit: ')
            P2_converted = converter(P2) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2)
            T2 = input('Please type the value of the Final Temperature along with its unit (K or C): ')
            T2_converted = converter_03(T2)
            print('Processing')
            answer = (P1_converted * V1_converted * T2_converted) / (P2_converted * V2_converted)
            print('The Initial Temperature is ' + str(answer) + ' Kelvin')
            os.system('pause')
            problem_solver() #Takes the user back to the selection point
        elif (CGLDerive.upper() == 'G U G G G G') or (CGLDerive.upper() == 'GUGGGG'):
            P1 = input('Please type the value of the Initial Presssure along with its unit: ')
            P1_converted = converter(P1) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            T1 = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T1_converted = converter_03(T1)
            P2 = input('Please type the value of the Final Pressure along with its unit: ')
            P2_converted = converter(P2) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2)
            T2 = input('Please type the value of the Final Temperature along with its unit (K or C): ')
            T2_converted = converter_03(T2)
            print('Processing')
            answer = (P2_converted * V2_converted * T1_converted) / (T2_converted * P1_converted)
            print('The Initial Volume is ' + str(answer) + ' Liters')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (CGLDerive.upper() == 'U G G G G G') or (CGLDerive.upper() == 'UGGGGG'):
            V1 = input('Please type the value of the Initial Volume along with its unit (L or ml): ')
            V1_converted = converter_02(V1)
            T1 = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T1_converted = converter_03(T1)
            P2 = input('Please type the value of the Final Pressure along with its unit: ')
            P2_converted = converter(P2) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V2 = input('Please type the value of the Final Volume along with its unit (L or ml): ')
            V2_converted = converter_02(V2)
            T2 = input('Please type the value of the Final Temperature along with its unit (K or C): ')
            T2_converted = converter_03(T2)
            print('Processing')
            answer = (P2_converted * V2_converted * T1_converted) / (T2_converted * V1_converted)
            print('The Initial Pressure is ' + str(answer) + ' atm')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        else:
            print('Given the choice you gave, no possible equations are available to solve it.')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
    elif (selection == 'f') or (selection == 'F'):
        print("Ideal Gas Law (PV = nRT)")
        print('There are four Variables and One Constant \n Pressure, Volume, Mole amount of a gas or certain element, and Temperature are the Variables (P, V, n, and T respectiveley) \n The Gas Constant (R) is... yeah. Constant (0.0821 L*atm/mol*k).')
        print('Please Type what Variables are Given and What is missing and same format as below:')
        print('G G G U = P, V and n is Given, T is Missing or Unknown')
        print('G G U G = P, V and T is Given, n is Missing or Unknown')
        print('G U G G = P, n and T is Given, V is Missing or Unknown')
        print('U G G G = V, n and T is Given, P is Missing or Unknown')
        IGLDerive = input("Please type what are the Given and the Unknown: ")
        if (IGLDerive.upper() == 'G G G U') or (IGLDerive.upper() == 'GGGU'):
            P = input('Please type the value of the given Presssure along with its unit: ')
            P_converted = converter(P) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V = input('Please type the value of the given Volume along with its unit (L or ml): ')
            V_converted = converter_02(V)
            print('Did the problem gave you a molar mass in g/mol? or molecular weight in g?')
            moles_or_grams = input("Type 'a' if it gave you molar mass in g/mol and 'b' if it gave you molecular weight in g: ")
            if (moles_or_grams.upper() == 'A'):
                n = input('Please type the given Molar value in g/mol: ')
                n_converted = converter_04(n)
            elif (moles_or_grams.upper() == 'B'):
                weight = input('Please type the weight in grams (g): ')
                weight_converted = converter_06(weight)
                compound = input('Please type the Chemical Formula: ')
                molar_mass = converter_05(compound)
                n_converted = weight_converted / float(molar_mass)
            print('Processing')
            answer = (P_converted * V_converted) / (n_converted * R)
            print('The calculated Temperature is ' + str(answer) + ' Kelvin')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        if (IGLDerive.upper() == 'G G U G') or (IGLDerive.upper() == 'GGUG'):
            P = input('Please type the value of the given Presssure along with its unit: ')
            P_converted = converter(P) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            V = input('Please type the value of the given Volume along with its unit (L or ml): ')
            V_converted = converter_02(V)
            T = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T_converted = converter_03(T)
            print('Processing')
            answer = (P_converted * V_converted) / (R * T_converted)
            print('The Calculated Moles of gas is ' + str(answer) + ' g/mol')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        if (IGLDerive.upper() == 'G U G G') or (IGLDerive.upper() == 'GUGG'):
            P = input('Please type the value of the given Presssure along with its unit: ')
            P_converted = converter(P) # Conversion of all Pressures into atm(Standard Atmospheric Pressure)
            print('Did the problem gave you a molar mass in g/mol? or molecular weight in g?')
            moles_or_grams = input("Type 'a' if it gave you molar mass in g/mol and 'b' if it gave you molecular weight in g: ")
            if (moles_or_grams.upper() == 'A'):
                n = input('Please type the given Molar value in g/mol: ')
                n_converted = converter_04(n)
            elif (moles_or_grams.upper() == 'B'):
                weight = input('Please type the weight in grams (g): ')
                weight_converted = converter_06(weight)
                compound = input('Please type the Chemical Formula: ')
                molar_mass = converter_05(compound)
                n_converted = weight_converted / float(molar_mass)
            T = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T_converted = converter_03(T)
            print('Processing')
            answer = (n_converted * R * T_converted) / P_converted
            print('The calculated amount of Volume is ' + str(answer) + ' Liters')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        if (IGLDerive.upper() == 'U G G G') or (IGLDerive.upper() == 'UGGG'):
            V = input('Please type the value of the given Volume along with its unit (L or ml): ')
            V_converted = converter_02(V)
            print('Did the problem gave you a molar mass in g/mol? or molecular weight in g?')
            moles_or_grams = input("Type 'a' if it gave you molar mass in g/mol and 'b' if it gave you molecular weight in g: ")
            if (moles_or_grams.upper() == 'A'):
                n = input('Please type the given Molar value in g/mol: ')
                n_converted = converter_04(n)
            elif (moles_or_grams.upper() == 'B'):
                weight = input('Please type the weight in grams (g): ')
                weight_converted = converter_06(weight)
                compound = input('Please type the Chemical Formula: ')
                molar_mass = converter_05(compound)
                n_converted = weight_converted / float(molar_mass)
            T = input('Please type the value of the Initial Temperature along with its unit (K or C): ')
            T_converted = converter_03(T)
            print('Processing')
            answer = (n_converted * R * T_converted) / V_converted
            print('The calculated amount of pressure is ' + str(answer) + ' atm')
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        else:
            print('Given the choice you gave, no possible equations are available to solve it.')
            os.system('pause')
            os.system('cls')
    elif (selection == 'g') or (selection == 'G'):
        print("Dalton's Partial Pressure")
        print('Really? You also want to use this one? You might just use a calculator though. \n Anyways, if you really need to-')
        Number_of_PPs = input('How many partial pressures are in the problem?\n NOTE: DO NOT INCLUDE THE TOTAL PRESSURE IF THAT IS GIVEN IN THE PROBLEM \n THAT WILL JUST GIVE YOU TROUBLE THOUGH.: ')
        if (Number_of_PPs != 0):
            limit = 0
            PPs_Stored = []
            while (limit != int(Number_of_PPs)):
                Partial_Pressure = input('Type the Partial Pressure (PP) Here \n NOTE: One PP at a time: ')
                Converted_PP = converter(Partial_Pressure)
                PPs_Stored.append(Converted_PP)
                limit += 1
            print('Here: ' + str(sum(PPs_Stored)))
            os.system('pause')
            os.system('cls')
            problem_solver() #Takes the user back to the selection point
        elif (Number_of_PPs == 0):
            print('Really? What do you want? I mean, for real though. ')
            os.system('pause')
            os.system('cls')
            problem_solver()

try:
    problem_solver()
except KeyboardInterrupt as e:
    print('Thank you for using the Program!')
    exit