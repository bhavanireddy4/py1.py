class Library:
  def __init__(self,list,name):
    self.book=list
    self.name=name
    self.lendDict={}

  def displayBook(self):
    print(f"we have following books in our library:{self.name}")
    for book in self.booklist:
      print(book)

  def lendBook(self,user,book):
    if book not in self.lendDict.keys():
      self.lendDict.update({book.user}) 
      print ("Lender-book database has been updated.you cantake the book now")
    else:
      print("bool is already in use by{self.lendDict[book]}")
  def addBook(self,book):
    self.booklist.append(book)
    print("book has been added to your list")
  def returnBook(self,book):
    self.lendDict.pop(book)
if __name__=='__main__':
    dnyanesh=Library(['python','c++','java','c'])
    while(True):
      print(f"welcome to the {dnyanesh.name}library.enter your choice to continue")
      print("1.Display")
      print("2.lendbooks")
      print("3.addbooks")
      print("4.returnbook")
      user_choice=input()
      if user_choice not in ['1','2','3','4']:
        continue
      else:
        user_choice=int(user_choice)

      if user_choice==1:
        dnyanesh.displaybooks()
      elif user_choice==2:
        book=input("enter the name of the book you want to lend:")
        user=input("enter your name")
        dnyanesh.lendBook(user,book)

      elif user_choice==3:
        book=input("enter the name of the book do you want to add:")
        dnyanesh.addBook(book)
      
      elif user_choice==4:
        book=input("enter the name of the book do you want to return:")
        dnyanesh.returnBook(book)
      else:
        print("not a valid option")

        print("press q to quit and c to continue")
        user_choice=input()
        if user_choice=="q":
          exit()





 


