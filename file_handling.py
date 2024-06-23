from pathlib import Path
from answer import Answer
from question import Question
from test import Test


def get_file_path():
    """
    Get the path to the test file from user input.
    """
    file_path = Path(input("Enter test file path: "))

    if file_path.is_file():
        return file_path

    raise FileNotFoundError


def read_lines_from_file(file_path: Path):
    """
    Generate lines of a file one at a time.
    """
    with open(file_path, 'r') as test_file:
        for line in test_file:
            yield line


def process_test(lines) -> Test:
    """
    Parse through the test file and store the contents of the test.
    """
    test = Test()
    current_question = None
    inside_question = False

    for line in lines:
        if line.startswith('Q'):
            current_question = Question(line[:-1])
            inside_question = True

        if inside_question and line == "\n":
            test.add_question(current_question)

            # Reset
            current_question = None
            inside_question = False

        if inside_question:
            if line.startswith('+') or line.startswith('-'):
                current_question.add_answer(Answer(line[:-1]))

    return test
