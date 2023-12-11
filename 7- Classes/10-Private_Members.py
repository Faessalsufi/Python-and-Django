class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self,tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(),0) + 1
    
    def __getitem__(self,tag):
        return self.__tags.get(tag.lower(),0)

    def __setitem__(self,tag,count):
         self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()

cloud.add("python")
cloud.add("pYtHoN")
cloud.add("PYTHON")
# print(cloud.__tags) #! Error
print(cloud.__dict__) #? to see the tags
print(cloud._TagCloud__tags) #imp Using this we can access private members 