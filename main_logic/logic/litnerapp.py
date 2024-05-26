from main_logic.logic.getdb import GetWordsFromDb
class MainLitnerApp:
    def __init__(self,username,datetime):
        self.words=GetWordsFromDb(username,datetime)

    def showwords(self):
        return self.words.getfromdatabase()
    