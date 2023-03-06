class Zajecia:
    def __init__(self):
        self.studenci = []    

    def zapiszStudenta(self, student):
        if len(self.studenci) < 10 : self.studenci.append(student)
        else: print("Lista jest pelna!!")

    def pokazListe(self):
        print(self.studenci)
