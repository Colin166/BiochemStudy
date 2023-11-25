'''
File : amino_acids_sequencing.py
Author : Colin Jones
Date : 9/18/2023
Description : Generates a user given length amino acid sequence then allows the user to sequence with various chemicals / methods.
'''

# Imports
import random
import re


# Function Definitions
def split_sequence (letters, sequence) :
    separators = '(' + '|'.join(letters) + ')'
    print("Sequencing from amino acids: " + separators)
    split_sequence = re.split((separators), sequence)
    new_sequence = []
    for n in range (0, len(split_sequence)-1, 2) :
        if not (n == 0 and letters == split_sequence[0]) :
            new_sequence_element = split_sequence[n] + split_sequence[n+1]
            new_sequence.append(new_sequence_element)
    new_sequence.append(split_sequence[len(split_sequence)-1])
    return new_sequence
def create_sequence (length) :
    sequence = []
    for i in range(sequence_length) :
        sequence.append(amino_acids[random.randint(0,19)])
    return sequence


# Polypeptide Creation
amino_acids = ['G', 'A', 'V', 'L', 'I', 'F', 'R', 'K', 'D', 'E', 'C', 'Q', 'S', 'T', 'W', 'Y', 'P', 'H', 'N', 'M']
sequence_length = int(input("How long would you like the sequence to be? "))
sequence_str = "".join(create_sequence(sequence_length))
print(sequence_str)


# Decide between sequencing and pH calculator.
choice = input("Would you like to sequence or calculate pH? Enter 1 for sequencing. Enter 2 for pH.")
if choice == "1" :
    print("Input 'STOP' to end experiment. Input NEW to generate a new polypeptide.")
    print("Choices of chemicals are PTH / Phenyl Isothiocyanate for N-terminus.")
    print("Choices of chemicals are Cyanogen Bromide, NH2OH, Trypsin, Chymotrypsin, Clostripain, Stahpylococcal Protease, and Endopeptidase Lys-C for middle.")
    print("Choices of chemicals are Carboypeptidase A, Carboxypeptidase B, Carboxypeptidase Y for C-terminus.")
    print("There is also the case at which 'pH is 2.5 & temp is 40C'")
    user_input = input("Please input your chemical / method here for sequencing: ")
    while user_input.lower() != 'stop' :
        print()
        match user_input.lower() :
            case "trypsin":
                print(split_sequence(["R", "K"], sequence_str))
            case "chymotrypsin" :
                print(split_sequence(["F", "Y", "W", "L"], sequence_str))
            case "clostripain" :
                print(split_sequence(["R"], sequence_str))
            case "cyanogen bromide" :
                print(split_sequence(["M"], sequence_str))
            case "pth" :
                print([sequence_str[0], sequence_str[1:len(sequence_str)]])
            case "phenyl isothiocyanate" :
                print([sequence_str[0], sequence_str[1:len(sequence_str)]])
            case "pth / phenyl isothiocyanate" :
                print([sequence_str[0], sequence_str[1:len(sequence_str)]])
            case "staphylococcal protease" :
                print(split_sequence(["D", "E"], sequence_str))
            case "endopeptidase lys-c" :
                print(split_sequence(["K"], sequence_str))
            case "carboxypeptidase a" :
                if sequence_str[len(sequence_str)-1] != "P"  or sequence_str[len(sequence_str)-1] != "R" or sequence_str[len(sequence_str)-1] != "E" or sequence_str[len(sequence_str)-1] != "D" or sequence_str[len(sequence_str)-1] != "K" : 
                    print([sequence_str[0:len(sequence_str) - 1], sequence_str[len(sequence_str)-1]])
            case "carboxypeptidase b" :
                if sequence_str[len(sequence_str)-1] == "R" or sequence_str[len(sequence_str)-1] == "K" :
                    print([sequence_str[0:len(sequence_str) - 1], sequence_str[len(sequence_str)-1]])
            case "carboxypeptidase y" :
                print([sequence_str[0:len(sequence_str) - 1], sequence_str[len(sequence_str)-1]])
            case "new" :
                sequence_str = "".join(create_sequence(int(input("How long would you like the sequence to be? "))))
                print(sequence_str)
        print()
        print("Enter 'STOP' to end experiment.")
        user_input = input("Please input your chemical / method here for sequencing: ")

elif choice == "2" :
    user_pH = float(input("Please input your pH: "))
    charge = 0
    for i in range(len(sequence_str)) :
        # Bases
        if i == 0 and user_pH < 9.1 :
            charge += 1
        if sequence_str[i] == 'K' and user_pH < 10.5 :
            charge += 1
        if sequence_str[i] == 'R' and user_pH < 12.4 :
            charge += 1
        if sequence_str[i] == 'H' and user_pH < 6.0 :
            charge += 1

        # Acids
        if sequence_str[i] == 'D' and user_pH > 3.86 :
            charge -= 1
        if sequence_str[i] == 'E' and user_pH > 4.25 :
            charge -= 1
        if sequence_str[i] == 'C' and user_pH > 8.33 :
            charge -= 1
        if sequence_str[i] == 'Y' and user_pH > 10 :
            charge -= 1
        if i == len(sequence_str) - 1 and user_pH > 2.2 :
            charge -= 1
    
    print("Your polypeptide's charge is: ")
    print(str(charge))
        

else :
    print("Not a valid input.")