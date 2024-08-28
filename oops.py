
class FileManaging:
    def __init__(self,filename):
        self.file = filename

    def write_file(self,sent):
        f=open(self.file,"w")
        f.write(sent)
        f.close()


class FileOperation(FileManaging):
    def __init__(self,file):
        super().__init__(file)
    def userinput(self):
        sent = input(("enter the content"))
        self.write_file(sent)

file = "user_content.txt"
x = FileOperation(file)
x.userinput()
