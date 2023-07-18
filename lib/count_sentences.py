#!/usr/bin/env python3

import ipdb
import re

class MyString:

  count = 0

  def __init__(self, value=""):
    self.value = value

  def set_value(self):
    return self._value
  
  def get_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")

  value = property(set_value, get_value)

  def is_sentence(self):
    if self._value.endswith('.'):
      return True
    else:
      return False
  
  def is_question(self):
    if self._value.endswith('?'):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self._value.endswith('!'):
      return True
    else:
      return False
    
  def count_sentences(self):
    new_list = []
    if self._value != 0:
      sen = re.split('[.!?]', self._value)
      new_list = [word for word in sen if word != ""]
      return len(new_list)
    

#count_sentences = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
#print(count_sentences())