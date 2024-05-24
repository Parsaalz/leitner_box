class Countword_Class:
    def __init__(self,string):
        self.string=string
    def display_number_of_words(self):
        counter=0
        for i in range(len(self.string)-1):
            if self.string[i] == ' ' and self.string[i+1]!=' ':
                counter+=1
        return counter
    