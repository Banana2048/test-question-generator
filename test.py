from question import Question


class Test:
    def __init__(self):
        """
        Initialize an empty list of questions.
        """
        self._questions = []

    def questions(self) -> list[Question]:
        """
        Return the list of questions.
        """
        return self._questions

    def add_question(self, question: Question):
        """
        Add a question to the test.
        """
        self._questions.append(question)


    def shuffle_questions(self):
        """
        Shuffle the list of questions.
        """
        import random
        indexes = list(range(len(self._questions)))
        shuffled_questions = []

        for i in range(len(self._questions)):
            # generate random indexes
            random_index = random.randrange(0, len(indexes))
            random_question_index = indexes[random_index]

            # shuffle answers & add question to shuffled questions
            current_question = self.questions()[random_question_index]
            current_question.shuffle_answers()
            shuffled_questions.append(current_question)

            # remove index from indexes
            indexes.pop(random_index)

        self._questions = shuffled_questions

    def display_test(self):
        """
        Print the questions & answers of the test.
        """
        current_question = 1
        answer_index = 0
        answer_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        print('==TEST==')
        for question in self.questions():
            print(f'{current_question}. {question.question()}')

            for answer in question.answers():
                print(f'{answer_options[answer_index]}) {answer.answer()}')
                answer_index += 1

            current_question += 1
            answer_index = 0

            print()

    def display_answer_key(self):
        """
        Print the correct answer for each question.
        """
        current_question = 1
        answer_options = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        print('== ANSWER KEY ==')
        for question in self.questions():
            correct_answers = []
            for answer_index in range(len(question.answers())):
                if question.answers()[answer_index].is_correct():
                    correct_answers.append(answer_options[answer_index])
            
            if len(correct_answers) == 1:
                print(f'{current_question}. {correct_answers[0]}')

            else:
                print(f'{current_question}.', end = " ")

                for i in range(len(correct_answers)):
                    print(f'{correct_answers[i]}', end = " ")
                    
                print()

            current_question += 1
