class Event:
  def __init__(self, name):
    self.name = name


  def set(self, func):
    self.func1 = func


  def user_defined(self, arg1):
    return self.func1(arg1)


  def test_local(self, arg):
    return arg+1
    
