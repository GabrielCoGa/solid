# SimpleResponsabiliteP SOC
#https://youtu.be/mWaZD8uztT8?si=FUS5XfEUEaHIkTnA

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

    def load(self, filename):
        pass

    def low_from_web(self, uri):
        pass


j= Journal()
j.add_entry('I cried toda.')
j.add_entry('I ete a bug.')
print(f'Journal entries:\n{j}')

file = r'c:\temp\journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())