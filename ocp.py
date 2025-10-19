#OpenCloseP
#https://youtu.be/mWaZD8uztT8?si=FUS5XfEUEaHIkTnA

from enum import Enum
#from zipfile import sizeCentralDir

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_color_and_size(self, products, color, size):
        for p in products:
            if p.color == color and p.size == size:
                yield p

# Enterprise Patterns: Specification

class Specification:
    def is_satisfied(self, item):
        pass
#modificacion para estudiar porque lo hace
    def __add__(self, other):
        return AndSpecification(self,other)

class Filter:
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, item):
        return  self.spec1.is_satisfied(item) and \
                self.spec2.is_satisfied(item)

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

products = [apple, tree, house]

print('Green productos(old):')
#Instanciamos la clase ProductFilter
pf = ProductFilter()
for po in pf.filter_by_color(products, Color.GREEN):
        print(f'- {po.name} is green')

print('Green products (new):')
#Instaciamos la clase BetterFilter
bf = BetterFilter()
#Instanciamos la clase ColorSpecification
green = ColorSpecification(Color.GREEN)
for pn in bf.filter(products, green):
    print(f'- {pn.name} is green')

print('Large products')
#Instanciamos la clase SizeSpecification
large = SizeSpecification(Size.LARGE)
for pnl in bf.filter(products, large):
    print(f'- {pnl.name} is large')

print('Large blue items')
#Instanciamos la clase AndSpecification
large_blue = AndSpecification(SizeSpecification(Size.LARGE), ColorSpecification(Color.BLUE))
for p in bf.filter(products, large_blue):
    print(f'- {p.name} is large and blue')

#modificacion que viene de arriba
large_blue_1 = SizeSpecification(Size.LARGE) and ColorSpecification(Color.BLUE)
for p in bf.filter(products, large_blue_1):
    print(f'- {p.name} is large and blue')
    