class Human:

    def __init__(self,name):
        self.human_name=name 
    def get_name(self):
        return self.human_name

h=Human('michal')
print(h.get_name())
