# class parent(object):
#     def __init__(self) -> None:
#         pass

# class child(parent):
#     def __init__(self) -> None:
#         super().__init__()


# def vivek(name) -> str:
#     return name
# print(vivek("vishal"))

class person:
    def __init__(self,game) -> None:
        self.game = game 
        self.special = 'This is something new'

class boii(person):
    def __init__(self, game, hobbies) -> None:
        self.hobby = hobbies
        super().__init__(game)

b1 = boii('football','cycling')

print(b1.hobby,b1.special,b1.game,sep="\n")