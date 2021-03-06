#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)
    #this is how to create decorators, and from my understanding allow objects to control data
    #also they allow one to access class functions like attributes
    @property
    def color(self):
        return  self.properties.get('color',None)
    
    @color.setter
    def color(self,c):
        self.properties['color']=c
    
    @color.deleter
    def  color(self):
        del self.properties['color']

def main():
    donald = Duck()
    donald.color='blue' # see here how we call functions like attributes
    print(donald.color)

if __name__ == "__main__": main()
