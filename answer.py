class Answer:
    def __init__(self, answer: str):
        """
        Initialize the answer and determine its correctness.
        """
        self._answer = answer[1:]
        self._is_correct = answer.startswith('+') or answer.startswith('*')

    def answer(self) -> str:
        """
        Return the answer as a string.
        """
        return self._answer

    def is_correct(self) -> bool:
        """
        Return whether the answer is correct.
        """
        return self._is_correct