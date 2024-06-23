from answer import Answer


class Question:
    def __init__(self, question: str):
        """
        Initialize the question & an empty list of answers.
        """
        self._question = question[2:]
        self._answers = []

    def question(self) -> str:
        """
        Return the question as a string.
        """
        return self._question

    def answers(self) -> list[Answer]:
        """
        Return the list of answers.
        """
        return self._answers

    def add_answer(self, answer: Answer):
        """
        Add an answer to the list of answers.
        """
        self._answers.append(answer)

    def shuffle_answers(self):
        """
        Shuffle the answers to the question.
        """
        import random
        num_of_answers = len(self._answers)
        indexes = list(range(num_of_answers))
        shuffled_answers = []

        for i in range(num_of_answers):
            random_index = random.randrange(len(indexes))
            random_answer_index = indexes[random_index]
            shuffled_answers.append(self.answers()[random_answer_index])
            indexes.pop(random_index)

        self._answers = shuffled_answers
