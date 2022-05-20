
# context manager using class
class ManagedFile:
    def __init__(self, filename):
        print('init ', filename)
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

        if exc_type is not None:
            print("Exception has been handled")
        print('exit')
        return True


with ManagedFile('notes.txt') as file:
    file.write('some todo....')


# context manager using function
from contextlib import contextmanager


@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()


with open_managed_file('notes.txt') as f:
    f.write('Some to do')

