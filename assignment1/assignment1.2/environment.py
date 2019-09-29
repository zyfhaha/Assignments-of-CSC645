class environment():
    def __init__(self,length,cleanliness):
        self.length=length
        self.cleanliness=cleanliness
    def droplitter(self,position):
        self.cleanliness[position]=1;
    pass