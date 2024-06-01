class TextEditor:

    def __init__(self):
        self._content = ''
        self._mementos = []

    def type(self, text):
        self._content += text
        self._mementos.append(TextEditorMemento(self._content))

    def undo(self):
        if len(self._mementos) > 0:
            self._content = self._mementos.pop().get_content()

    def get_content(self):
        return self._content


class TextEditorMemento:

    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content


if __name__ == '__main__':
    editor = TextEditor()
    editor.type('Hello')
    print(f'Editor content: {editor.get_content()}')
    editor.type(' World')
    print(f'Editor content: {editor.get_content()}')
    editor.undo()
    print(f'Editor content: {editor.get_content()}')
    editor.undo()
    print(f'Editor content: {editor.get_content()}')