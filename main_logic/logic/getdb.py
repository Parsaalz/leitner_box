from ..models import LitnerApp
class GetWordsFromDb:
    def __init__(self,username,date):
        self.username=username
        self.date=date

    def getfromdatabase(self):
        vocabs=LitnerApp.objects.filter(dl__lte=self.date,user=self.username,show=True)
        return vocabs