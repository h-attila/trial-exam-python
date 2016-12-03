# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.


def letterCounter(fileName):

    try:
        inputFile = open(fileName, 'r')
        fileText = inputFile.read()
        inputFile.close()
        return fileText.count('a')

    except FileNotFoundError:
        return 0


print(letterCounter('file_for_exercise_2.txt'))
print(letterCounter('fake_file_name.txt'))