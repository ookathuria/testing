from math import floor

class non_repeating_char:

    def __init__(self):

        self.nonRepeatingChar()

    def nonRepeatingChar(self):

        string = input("Enter the string to analyze for first non-repeating character : ")

        i=0
        j = 0
        dict = {}
        for i in range(len(string)):
            if string[i] not in dict:
                dict[string[i]]=[i]
            else:
                dict[string[i]].append(i)

        print(dict)

        for character in dict:
            if len(dict[character]) == 1:
                print('character is : ',character,'\n','postion is : ',dict[character])
                break


def main():
    nrc = non_repeating_char()

if __name__ == '__main__':
    main()