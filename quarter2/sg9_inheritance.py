class Publication:
  def __init__(self, title, author):
    self.__title = title
    self.__author = author

  def get_title(self):
    return self.__title

  def set_title(self, title):
    self.__title = title

  def get_author(self):
    return self.__author

  def set_author(self, author):
    self.__author = author

  def display_info(self):
    print("Title: ", self.__title)
    print("Author: ", self.__author)

class Book(Publication):
  def __init__
