from ..models import LitnerApp
from datetime import datetime,timedelta
class HandleAnswer:
    def __init__(self,user,word_id):
        self.word_id=word_id
        self.user=user

    def correctanswer(self):
        word=LitnerApp.objects.get(id=self.word_id,user=self.user)
        word.level+=1
        if word.level==1:
            current_day=datetime.now().strftime("%Y-%m-%d")
            current_day=datetime.strptime(current_day, "%Y-%m-%d")
            next_time=timedelta(days=1)
            next_time=current_day+next_time
            word.dl=next_time
        elif word.level==2:
            current_day=datetime.now().strftime("%Y-%m-%d")
            current_day=datetime.strptime(current_day, "%Y-%m-%d")
            next_time=timedelta(days=2)
            next_time=current_day+next_time
            word.dl=next_time
        elif word.level==3:
            current_day=datetime.now().strftime("%Y-%m-%d")
            current_day=datetime.strptime(current_day, "%Y-%m-%d")
            next_time=timedelta(days=4)
            next_time=current_day+next_time
            word.dl=next_time
        else:
            word.show=False
        word.save()
        return 1
    

    def WrongAnswer(self):
        wr=LitnerApp.objects.get(id=self.word_id,user=self.user)
        current_day=datetime.now().strftime("%Y-%m-%d")
        current_day=datetime.strptime(current_day, "%Y-%m-%d")
        next_time=timedelta(days=1)
        next_time=current_day+next_time
        wr.dl=next_time
        wr.level=0
        wr.save()
        return 1
