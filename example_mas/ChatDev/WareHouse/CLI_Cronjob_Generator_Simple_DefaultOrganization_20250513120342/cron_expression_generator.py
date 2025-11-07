'''
Utility class for generating cron expressions based on user input.
'''
class CronExpressionGenerator:
    @staticmethod
    def generate_expression(schedule):
        '''
        Generates a cron expression based on the selected schedule.
        :param schedule: The selected schedule option.
        :return: The corresponding cron expression.
        '''
        cron_expressions = {
            "daily_3am": "0 3 * * *",
            "every_15_minutes": "*/15 * * * *",
            "hourly": "0 * * * *",
            "weekly": "0 0 * * 0"
        }
        return cron_expressions.get(schedule, "")