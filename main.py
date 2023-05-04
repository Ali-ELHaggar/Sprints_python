# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def mutate_string(string, position, character):
    """ this function accepts three parameters and changes the imdex specified by user to his required character"""
    x = list(string)
    x[position] = character
    string = ''.join(x)
    print(string)


mutate_string("abracadabra", 5, "k")
