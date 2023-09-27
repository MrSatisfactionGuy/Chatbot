import re
import long_responses as long

def msgProbability(userMsg, recognizeWord, singleRespo=False, requieredWords=[])
    msgCertainty = 0
    hasRequieredWord = True

    #count how many words are present in each message
    for word in userMsg:
        if word in recognizeWord:
            msgCertainty += 1

    #calculate the percentage of recognized words in a user message
    percentage = float(msgCertainty) / float(len(recognizeWord))

    for word in requieredWords:
        if word not in userMsg:
            hasRequieredWord = False
            break

    if hasRequieredWord or singleRespo:
        return int(percentage*100)
    else:
        return 0
    
def checkAllMsg(msg):
    highestProbList = {}

    def response(botResponse, listOfWord, singleRespo=False, requiredWord=[]):
        nonlocal highestProbList
        highestProbList[botResponse] = msgProbability(msg, listOfWord, singleRespo, requiredWord)

    #Response -----------------------------------
    response('Hello!', ['hello', 'hi', 'heya', 'heyo'], singleRespo=True)
    response('Im doing fine, and you?', ['how','are','you',], requiredWord=['how','are','you'])
    #response('Thank you!', [])

    bestMatch = max(highestProbList, key=highestProbList.get())
    print(highestProbList)

    return bestMatch

def getResponse(userInput):
    splitMsg = re.split(r'\s+|[,;?!.-]\s*', userInput.lower())
    response = checkAllMsg(splitMsg)
    return response


#Testing the response system
while True:
    print('Bot: ' + getResponse(input('You: ')))