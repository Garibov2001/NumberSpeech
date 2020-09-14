

# Divides the sent number into tens, for example (2587 = 2000 + 500 + 80 + 7 )
# Then creates list with these numbers (["2000", "500", "80", "7"])
def SeperateNumber(argNumber):
    argNumber = str(argNumber)
    seperateList = []
    length = len(argNumber)
    counter = length - 1 

    for i in range(length):
        tempNum = argNumber[i] + "0"*counter
        if(argNumber[i] != "0"):
            seperateList.append(tempNum)
        counter -= 1

    return seperateList


# Counts the number of zeros in the sent number
def ZeroCounter(argNumber):
    argNumber = str(argNumber)
    counter = 0
    for number in argNumber:
        if(number == "0"):
            counter += 1
    return counter


# entry point of program
def NumberSpeech(argNumber):
    
    if(argNumber == "0"):
        return "sıfır"

    # The speech of numbers in Azerbaijani 
    numberSpeech = {
        "1":"bir",
        "2":"iki",
        "3":"üç",
        "4":"dörd",
        "5":"beş",
        "6":"altı",
        "7":"yeddi",
        "8":"səkkiz",
        "9":"doqquz"
    }

    # The speech of numbers in Azerbaijani
    numberSpeechInTen = {
        "1":"on",
        "2":"iyimi",
        "3":"otuz",
        "4":"qırx",
        "5":"əlli",
        "6":"altmış",
        "7":"yetmiş",
        "8":"səksən",
        "9":"doxsan"
    }
    
    tempList = SeperateNumber(argNumber)
    speech = ""


    for number in tempList:        
        if(ZeroCounter(number) == 0 ):
            speech += numberSpeech[number[0]] + " "
        else:
            if(ZeroCounter(number) == 1 ):
                speech += numberSpeechInTen[number[0]] + " "
            else:
                if(ZeroCounter(number) == 2 ):
                    if(number[0] == "1"):
                        speech += "yuz "
                    else:
                        speech += numberSpeech[number[0]] + " yüz "
                else:
                    if(ZeroCounter(number) == 3 ):
                        if(number[0] == "1"):
                            speech += "min "
                        else:
                            speech += numberSpeech[number[0]] + " min "
    return speech






