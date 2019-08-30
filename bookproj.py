#%%

from string import Template

books = open('booklist.txt', 'r')

booklist = []

# create the booklist

for line in books:
    book = line.split(',')
    booklist.append(book)


peopleDict = {}
nameList = []
ratingList = []

# create the namelist and ratingList


peopleRating = open('ratings.txt', 'r')
for line in peopleRating:
    if len(line) > 30:
        ratingList.append(line)
    else:
        nameList.append(line)

# create the peopleDict

h = 0
positiveRatingsDict = {}
# print(ratingList[0].split()[1])
# while h < len(booklist) :
#     bookName = booklist[h][0] + ', ' + booklist[h][1]
#     # print(bookName)
#     j = 0
#     while j < len(ratingList[j].split()) :
#         if int(ratingList[j].split()[h]) > 0:
#             bookRatings[bookName] = ratingList[j].split()[h]
        
#         # print(bookRatings)
#         k = 0
#         while k < len(nameList):
#             peopleRatingsDict[nameList[k].lower()] = bookRatings
#             k +=1
           
#         j += 1
#     # print(peopleDict[nameList[i]])
#     h += 1
# print(nameList)
# print(booklist)
# print(ratingList)
while h < len(nameList) :
    personName = nameList[h]
    # print(bookName)
    k = 0
    bookRatingList = ratingList[h].split()
    bookRatings = {}
    # print(bookRatingList)
    while k < len(booklist):
        bookName = booklist[k][0] + ', ' + booklist[k][1]
        bookRating = bookRatingList[k]
        # print(bookRating)
        if int(bookRating) > 2:
            # print(bookName, bookRating)
            bookRatings[bookName] = bookRating
            positiveRatingsDict[personName.lower()] = bookRatings
            # print(bookName, bookRatings[bookName])
            # print(bookRatings)
        k +=1
    # positiveRatingsDict[personName.lower()] = bookRatings
    # print(personName.lower(), positiveRatingsDict[personName.lower()])
    # print(peopleDict[nameList[i]])
    h += 1

# print(positiveRatingsDict['joe\n'])



i = 0

while i < len(nameList):
    peopleDict[nameList[i]] = ratingList[i].split()
    i += 1


def friends(name, nfriends = 2):
    nameRatings = peopleDict[name + '\n']
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
    names = friends(name, nfriends)
    # print('names: ', names)
    i = 0
    otherUsersBooks = []
    userBooks = []
    while i <= nfriends - 1 :
        
        friendsBooks = positiveRatingsDict[names[i]]
        userBooks.extend(positiveRatingsDict[name.lower() + '\n'])
        i += 1
        otherUsersBooks.extend(sorted(friendsBooks))
    
    recommendedBooks = []
    i = 0
    while i < len(otherUsersBooks):
        # print(otherUsersBooks[i])
        selectedBook = otherUsersBooks[i]
        if selectedBook not in userBooks:
            recommendedBooks.append(tuple(selectedBook.split(',')))
        i+=1

    sortedRecommendedBooks = sorted(recommendedBooks, key=lambda x: x[0].split()[-1])

    outputLine1 = Template('$name: $friends \n')

    output = open('recommendations.txt', 'w')

    output.write(outputLine1.substitute(name=name, friends=names))
    
    outputBookLine = Template('$bookline \n') 

    # print(recommendedBooks)

    for line in sortedRecommendedBooks:
        output.write(outputBookLine.substitute(bookline=line))

    # print('mine', userBooks)
    # for friendsBook in friendsBooks:
    #     print(friendsBook)
    #     for userBook in userBooks:

    # print(name, userBooks)

recommend("Albus Dumbledore")








# const bookList = [['Book 1', 'some Author'], ['Book 2', 'some Author'], ['Book 3', 'some Author']];

# const ratingList = [[0, 3, 5], [3, 0, 5]];

# const nameList = ['Preston', 'Blake'];

# function getRatings() {
# 	let personIndex = 0;
# 	const returnObj = {};
# 	while (personIndex < nameList.length) {
# 		const personName = nameList[personIndex];
# 		const ratings = ratingList[personIndex];

# 		let bookIndex = 0;
# 		while (bookIndex < bookList.length) {
# 			const book = bookList[bookIndex];
# 			const bookName = `${book[0]}, ${book[1]}`;
# 			const rating = ratings[bookIndex];

# 			if (rating > 0) {
# 				if (!returnObj[personName]) {
# 					returnObj[personName] = {};
# 				}

# 				returnObj[personName][bookName] = rating;
# 			}

# 			bookIndex += 1;
# 		}

# 		personIndex += 1;
# 	}

# 	return returnObj;
# }

# const ratingsObj = getRatings();
# console.log(JSON.stringify(ratingsObj, null, 2));

# /*
# Desired Output

# Is the book array correct? Why are the elements in the book array arrays themselves?
# Oh, I just looked at mine, I'll fix it
# 👍

# {
# 	"Preston": {
# 		"Book 2, some Author": 3,
# 		"Book 3, some Author": 5,
# 	}, 
# 	"Blake" : {
# 		"Book 1, some Author": 3,
# 		"Book 3, some Author": 5
# 	}
# }

# */


