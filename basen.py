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
    Python documentation can be written like this for the help() command
    
    Function: base_n
    Inputs: inputNumber, a decimal int. baseValue, an int.
    Preconditions: inputNumber or baseValue are both positive numbers. 
    Output: outputNumber, a string.
    Postconditions: inputNumber will be converted into decimal if necessary, converted to baseValue and then returned as outputNumber.
    """
    if baseValue >= 11 or baseValue <=15 or baseValue > 17:
        return "Incorrect base value supplied, please use 2,8,10,16"

    outputNumber = ""

    ##convert input to decimal here

    if inputNumber == 0:
        return [0]
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