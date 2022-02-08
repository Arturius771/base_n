#=======================================#
#Project Name: base_n "Basin"
#Date Started: 31/01/2022
#Date Completed: ongoing
#Artúr Foden
#www.arturfoden.ie
#=======================================#
#Take an input and return it in a given base
#=======================================#
#Language + Version: Python 3.10
#IDE + Version: VS Code 1.63.2
#Project Version: v1
#Lines of Code:
#=======================================#
#Convert the input into decimal. 
#While the number is greater than 1, 
#divide inputNumber by the base and 
#take the remainder. 
#Convert the given remainder
#=======================================#
#Modified:
#=======================================#

def base_n(inputNumber: int, baseValue: int) -> str:
    """
    This function converts any positive int value into another base, between 2 to 16
    
    Function: base_n
    Inputs: inputNumber, a decimal int. baseValue, an int.
    Preconditions: 0 <= inputNumber, 2 <= baseValue <= 16
    Output: outputNumber, a string.
    Postconditions: inputNumber will be converted into decimal if necessary, converted to baseValue and then returned as outputNumber.
    """
    if inputNumber >= 0 and 2 <= baseValue <= 16:

        outputNumber = ""

        ##convert input to decimal here

        if inputNumber == 0:
            return inputNumber
        while inputNumber >= 1:
            remainder = inputNumber % baseValue
            if remainder >= 10:
                if remainder >= 11: 
                    if remainder >= 12: 
                        if remainder >= 13:
                            if remainder >= 14: 
                                if remainder == 15:
                                    outputNumber = "F" + outputNumber
                                else:
                                    outputNumber = "E" + outputNumber
                            else:
                                outputNumber = "D" + outputNumber
                        else:
                            outputNumber = "C" + outputNumber
                    else:
                        outputNumber = "B" + outputNumber
                else:
                    outputNumber = "A" + outputNumber
            else:
                outputNumber = "{}".format(remainder) + outputNumber
            inputNumber //= baseValue
            print(outputNumber)            
        return outputNumber
    else:
        print("Enter valid input, please use the help() command if necessary")