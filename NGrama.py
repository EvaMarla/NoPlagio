import numpy as numpy

class NGrama:
  
  def __init__(self, size, words=None):
    self.__size   = size
    self.__words  = None
    if words is not None: self.setWords(words)
    else: self.__words = numpy.empty(self.__size, dtype=str) 
  
  def __str__(self):
    return " ".join(self.__words)

  def __repr__(self):
    return "{0},{1},{2}".format(self.__class__.__name__,'(', self.__size, tuple(self.__words), ')')
  
  def setWords(self, words):
    if(self.__size != len(words)):
      raise ValueError('List of words must be size: ' + str(self.__size))
    self.__words  = numpy.array(words, dtype=str)

#para testar
test = NGrama(2)
test.setWords(('cute', 'watermelon'))
print(test)
 print(test.__repr__())