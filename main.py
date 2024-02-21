
def alphabetLetterCount():
    tabArr = {}
    content = getFrankensteinContent().lower()
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
    for char in alphabet:
        currentCount = 0
        for charContent in content:
            if (charContent == char):
                currentCount += 1
        tabArr[char] = currentCount
    return tabArr

    
    

def getFrankensteinContent():
    content = ""
    # Open the file using with
    with open('./books/frankenstein.txt', 'r') as file:
        #Read the content of the file 
        content += file.read()
        # Print the content 
        # print(content)
        # words = len(content.split())
    return content


def getWords():
    content = getFrankensteinContent()
    return content.split()


def printReport():
    print('--- Begin report of books/frankenstein.txt ---')
    countWord = len(getWords())
    print(f'{countWord} words found in the document\n')
    alphabetLetterCounts = alphabetLetterCount() 
    for letter, letterCount in alphabetLetterCounts.items():
        print(f"The {letter} character was found {letterCount} times") 
    print('--- End report ---')

def main():
    printReport()


main()
