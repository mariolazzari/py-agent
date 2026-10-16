from functions.run_python_file import run_python_file


def main():
    print("Running main.py:")
    print(run_python_file("calculator", "main.py"))

    print('\nRunning main.py with "3 + 5":')
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("\nRunning tests.py:")
    print(run_python_file("calculator", "tests.py"))

    print("\nRunning ../main.py:")
    print(run_python_file("calculator", "../main.py"))

    print("\nRunning nonexistent.py:")
    print(run_python_file("calculator", "nonexistent.py"))

    print("\nRunning lorem.txt:")
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    main()
