
#imp If it walk as a duck quacks like a duck behaves like a duck then it is a duck
class TextBox():
    def draw(self):
        print("TextBox")


class DropDownList():
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
txt = TextBox()
# print(isinstance(ddl, UIControl))
draw([ddl,txt])