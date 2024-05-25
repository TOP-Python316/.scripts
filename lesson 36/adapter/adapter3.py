from abc import ABC, abstractmethod


# Интерфейс, который должен быть реализован для работы с файлами
class IFile(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


# Класс для работы с текстовыми файлами
class TextFile:
    def __init__(self, filename):
        self._filename = filename

    def read(self):
        with open(self._filename, "r") as file:
            return file.read()

    def write(self, data):
        with open(self._filename, "w") as file:
            file.write(data)


# Класс для работы с бинарными файлами
class BinaryFile:
    def __init__(self, filename):
        self._filename = filename

    def read(self):
        with open(self._filename, "rb") as file:
            return file.read()

    def write(self, data):
        with open(self._filename, "wb") as file:
            file.write(data)


# Класс-адаптер для работы с текстовыми файлами через интерфейс IFile
class TextFileAdapter(IFile):
    def __init__(self, filename):
        self._file = TextFile(filename)

    def read(self):
        return self._file.read()

    def write(self, data):
        self._file.write(data)


# Класс-адаптер для работы с бинарными файлами через интерфейс IFile
class BinaryFileAdapter(IFile):
    def __init__(self, filename):
        self._file = BinaryFile(filename)

    def read(self):
        return self._file.read()

    def write(self, data):
        self._file.write(data)


# Пример использования
if __name__ == "__main__":
    text_file = TextFileAdapter("example.txt")
    binary_file = BinaryFileAdapter("example.bin")

    data = "Hello, World!"
    text_file.write(data)
    print(text_file.read())

    binary_file.write(data.encode("utf-8"))
    print(binary_file.read().decode("utf-8"))
