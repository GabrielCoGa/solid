#InterfaceSegregationPrinciple
#https://youtu.be/mWaZD8uztT8?si=FUS5XfEUEaHIkTnA

from abc import abstractmethod

class Machine: #Interface
    def print(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError

class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

 #this class break de principle
class OldFashionedPrinter(Machine):
    def print(self, document):
        pass
        #ok

    def fax(self, document):
        pass
        #noop, do nothing

    def scan(self, document):
        #pass
        raise NotImplementedError('Printer cannot scan!')#other solution
#la solucion es dividir el interface en diferentes partes
class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class Fax:
    @abstractmethod
    def fax(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        scan(document)

#otra solucion con el patron decorador
class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass
    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    #patron decorador
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)