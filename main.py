from pathlib import Path
from file_handling import read_lines_from_file, process_test

def main():
    file_path = Path("test_file.txt") # input the desired text file to convert here
    test = process_test(read_lines_from_file(file_path))
    test.shuffle_questions()
    test.display_test()
    test.display_answer_key()


if __name__ == "__main__":
    main()