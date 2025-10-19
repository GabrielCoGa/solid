#DependencyInversionControlPrinciple
#https://youtu.be/mWaZD8uztT8?si=FUS5XfEUEaHIkTnA
from abc import abstractmethod
from enum import Enum

class RelationshipTipe(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser:#interface
    @abstractmethod
    def find_all_children_of(self, name):
        pass

#esta clase hereda del interface
class Relationship(RelationshipBrowser):#low-level module
    def __init__(self):
        self.relations = []
        '''Si cambiamos el tipo de almacenamiento, por ejemplo por un diccionario
        el programa crask en la class Research, para arreglar esto creamos un interface
        RelationshipBrowser'''
    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, RelationshipTipe.PARENT, child))
        self.relations.append((child, RelationshipTipe.CHILD, parent))

    #implementamos el nuevo metodo, que seria el que cambia cada vez que sea necesario
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == RelationshipTipe.PARENT:
                yield r[2].name

#concreta implementacion para un tipo de almacenamiento de datos
class Research:# high-level modulo
    '''def __init__(self, relationships):
        relations = relationships.relations
        for r in relations:
            #print(f'{r[0].name}')
            if r[0].name == 'John' and r[1] == RelationshipTipe.PARENT:
                print(f'{r[0].name} has a child called {r[2].name}')
    '''
    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}')

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationship()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
'''A si evitamos depender de una interna implementacion'''