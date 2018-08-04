import random
from file_control.file_controller import FileController

class Run(object):
    def go(self):
        the_file = FileController("file-controlled.txt")
        with the_file:
            the_file.append(f"test 5")
        print(the_file)


if __name__ == "__main__":
    run = Run()
    run.go()