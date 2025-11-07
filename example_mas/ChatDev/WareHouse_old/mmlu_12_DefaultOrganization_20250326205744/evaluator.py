'''
Evaluator class for determining the moral correctness of scenarios.
'''
class ScenarioEvaluator:
    def evaluate(self, scenario1, scenario2):
        # Basic rules for evaluating moral correctness
        def is_morally_wrong(scenario):
            # Example criteria for moral wrongness
            if "harm" in scenario or "damage" in scenario or "hurt" in scenario:
                return True
            return False
        scenario1_wrong = is_morally_wrong(scenario1)
        scenario2_wrong = is_morally_wrong(scenario2)
        if scenario1_wrong and scenario2_wrong:
            return 0  # Wrong, Wrong
        elif scenario1_wrong and not scenario2_wrong:
            return 1  # Wrong, Not wrong
        elif not scenario1_wrong and scenario2_wrong:
            return 2  # Not wrong, Wrong
        else:
            return 3  # Not wrong, Not wrong