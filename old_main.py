import re
import long_responses as long

def msgProbability(userMsg, recognizeWord, singleRespo=False, requiredWord=[]):
    msgCertainty = 0
    hasRequieredWord = True

    #count how many words are present in each message
    for word in userMsg:
        if word in recognizeWord:
            msgCertainty += 1

    #calculate the percentage of recognized words in a user message
    percentage = float(msgCertainty) / float(len(recognizeWord))

    for word in requiredWord:
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
    response('Im doing fine, and you?', ['how','are','you',], requiredWord=['how','are'])
    response('Glad to hear that!', ['im', 'fine', 'too'], requiredWord=['fine'])
    response('Glad to hear that!', ['im', 'fine', 'too'], requiredWord=['fine', 'too'])
    response('Thank you!', ['great'], singleRespo=True)
    response('Goodbye!', ['thats','it'])
    response('Goodbye!', ['i','got', 'to', 'go'], requiredWord=['go'])
    response('Goodbye!', ['goodbye'], requiredWord=['goodbye'])

    bestMatch = max(highestProbList, key=highestProbList.get)
    #print(highestProbList)

    return bestMatch

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = checkAllMsg(split_message)
    return response

#Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))