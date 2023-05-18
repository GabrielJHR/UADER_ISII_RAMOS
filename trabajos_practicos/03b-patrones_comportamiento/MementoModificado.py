import os

class Memento:
    def __init__(self, content):
        self.content = content

class FileWriterUtility:
    def __init__(self):
        self.content = ""
        self.states = []

    def write(self, string):
        self.content += string

    def save(self):
        if len(self.states) == 4:
            self.states.pop(0)
        self.states.append(Memento(self.content))

    def undo(self):
        if len(self.states) == 0:
            return
        memento = self.states.pop()
        self.content = memento.content

class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, times=1):
        for i in range(times):
            writer.undo()

if __name__ == '__main__':
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility()

    print("Se graba algo y se salva")
    writer.write("Patrón Memento\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba algo más y se salva")
    writer.write("Patrón Singleton\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba algo más y se salva")
    writer.write("Patrón Factory\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba algo más y se salva")
    writer.write("Patrón Decorator\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se deshace una vez")
    caretaker.undo(writer)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se deshace una vez")
    caretaker.undo(writer)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se deshace 2 veces")
    caretaker.undo(writer, 2)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")