class student:
    def __init__(self,name,rank,point):
        self.name=name
        self.rank=rank
        self.point=point

#custom function
    def demofun(self):
         print("I am "+self.name)
         print("I got",self.rank)
         print("I secured"+self.point+"\n")

#create 4 object
st1 = student("steve",1,"100")
st2 = student("christ",2,"90")
st3 = student("mark",3,"76")
st4 = student("kate",4,"60")
#call the function using the object
st1.demofun()
st2.demofun()
st3.demofun()
st4.demofun()