def main():
    words = 0
    # Open the file using with
    with open('./books/frankenstein.txt', 'r') as file:
        #Read the content of the file 
        content = file.read()
        # Print the content 
        # print(content)
        words = len(content.split())
    return words

def numCharacters():
    

words = main()
print(words)
