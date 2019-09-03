#%%

# create the booklist

def createBooksList() :
    books = open('booklist.txt', 'r')
    returnList = []
    for line in books:
        book = line.split(',')
        returnList.append(book)
    # print(returnList)
    return returnList



# create the namelist and ratingList

def createRatingsList() :
    returnList = []
    peopleRating = open('ratings.txt', 'r')
    for line in peopleRating:
        if len(line) > 30:
            returnList.append(line)
    return returnList

def createNamesList():
    returnList = []
    peopleRating = open('ratings.txt', 'r')
    for line in peopleRating:
        if len(line) < 30:
            returnList.append(line)
    return returnList



# create the peopleDict

def createPeopleDict() :
    peopleDict = {}
    nameList = createNamesList()
    ratingList = createRatingsList()
    i = 0
    while i < len(nameList):
        peopleDict[nameList[i]] = ratingList[i].split()
        i += 1
    return peopleDict


def createPositiveRatingsDict():
    h = 0
    positiveRatingsDict = {}
    nameList = createNamesList()
    ratingList = createRatingsList()
    booklist = createBooksList()

    while h < len(nameList) :
        personName = nameList[h]
        k = 0
        bookRatingList = ratingList[h].split()
        bookRatings = {}

        while k < len(booklist):
            bookName = booklist[k][0] + ', ' + booklist[k][1]
            bookRating = bookRatingList[k]

            if int(bookRating) > 2:
                bookRatings[bookName] = bookRating
                positiveRatingsDict[personName.lower()] = bookRatings

            k +=1
        h += 1

    print(positiveRatingsDict)
    
    return positiveRatingsDict







def friends(name, nfriends = 2):
    peopleDict = createPeopleDict()


    nameRatings = peopleDict[name]
    matchStrength = {}
    for key in peopleDict:
        if key.lower() != name.lower() + '\n':
            otherPerson = peopleDict[key]
            j = 0
            matchNum = 0
            while j < len(nameRatings) - 1:
                matchNum += int(nameRatings[j]) * int(otherPerson[j])
                j +=1
            matchStrength[matchNum] = key.lower()
    orderedMatchStrength = sorted(matchStrength.items())
    k = 0
    friendsTuple = orderedMatchStrength[-int(nfriends):]
    friendsList = []
    while k < len(friendsTuple):
        friendsList.extend([friendsTuple[k][1].lower()])
        k += 1
    friendsList.sort()

    return(friendsList)

def recommend(name, nfriends = 2) :
    friendsNames = {}
    compiledRecommendations = {}

    names = friends(name, nfriends)
    friendsNames[name] = names
    positiveRatingsDict = createPositiveRatingsDict()


    i = 0
    otherUsersBooks = []
    userBooks = []
    while i <= nfriends - 1 :
        
        friendsBooks = positiveRatingsDict[names[i]]
        userBooks.extend(positiveRatingsDict[name.lower()])
        i += 1
        otherUsersBooks.extend(sorted(friendsBooks))
    
    recommendedBooks = []
    i = 0
    while i < len(otherUsersBooks):
        selectedBook = otherUsersBooks[i]

        if selectedBook not in userBooks and tuple(selectedBook.split(',')) not in recommendedBooks:
            recommendedBooks.append(tuple(selectedBook.split(',')))
        i+=1

    sortedRecommendedBooks = sorted(recommendedBooks, key=lambda x: x[0].split()[-1])
    compiledRecommendations[name] = sortedRecommendedBooks

    return compiledRecommendations


def main(nfriends = 2) :
    # from string import Template

    # output = open('recommendations.txt', 'w')

    # nameList = createNamesList()
    # name = nameList[-1]
    # # print(name)
    
    # friendsNames = friends(name)
    # compiledRecommendations = recommend(name, nfriends)
    # outputLine1 = Template('$name: $friends \n')
    # output.write(outputLine1.substitute(name=name[:-1], friends=friendsNames))
    # outputBookLine = Template('$bookline \n')
    # for book in compiledRecommendations[name]: 
    #     output.write(outputBookLine.substitute(bookline=book))  
    # output.write('\n')
    
    from string import Template

    output = open('recommendations.txt', 'w')

    nameList = createNamesList()

    for name in nameList:
        friendsNames = friends(name)
        # print(friendsNames)

        compiledRecommendations = recommend(name, nfriends)
        # print(compiledRecommendations)
        outputLine1 = Template('$name: $friends \n')
        output.write(outputLine1.substitute(name=name[:-1], friends=friendsNames))
        outputBookLine = Template('$bookline \n')
        for book in compiledRecommendations[name]: 
            output.write(outputBookLine.substitute(bookline=book))  
        output.write('\n')
    # print(compiledRecommendations)


main()
# recommend('Megan')





