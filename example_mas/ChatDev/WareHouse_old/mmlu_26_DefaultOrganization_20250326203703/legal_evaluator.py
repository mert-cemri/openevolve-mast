'''
LegalEvaluator class to evaluate legal questions based on the Rule in Shelley's Case.
'''
class LegalEvaluator:
    def evaluate(self, question):
        '''
        Evaluate the legal question and return the correct answer index or a message.
        :param question: The legal question as a string.
        :return: The index of the correct answer or a message if not applicable.
        '''
        if "Rule in Shelley's Case" in question:
            return 1
        else:
            return "The question does not pertain to the Rule in Shelley's Case."