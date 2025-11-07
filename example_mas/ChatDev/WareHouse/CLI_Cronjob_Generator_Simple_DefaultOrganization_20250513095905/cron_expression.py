'''
Cron expression generation logic for the CLI cronjob generator.
'''
# Define schedule constants
DAILY_3AM = "daily_3am"
EVERY_15_MINUTES = "every_15_minutes"
EVERY_HOUR = "every_hour"
WEEKLY_SUNDAY = "weekly_sunday"
class CronExpression:
    def __init__(self):
        self.minute = "*"
        self.hour = "*"
        self.day_of_month = "*"
        self.month = "*"
        self.day_of_week = "*"
        self.custom_expression = None
    def set_schedule(self, schedule):
        if schedule == DAILY_3AM:
            self.minute = "0"
            self.hour = "3"
            self.day_of_month = "*"
            self.month = "*"
            self.day_of_week = "*"
        elif schedule == EVERY_15_MINUTES:
            self.minute = "*/15"
            self.hour = "*"
            self.day_of_month = "*"
            self.month = "*"
            self.day_of_week = "*"
        elif schedule == EVERY_HOUR:
            self.minute = "0"
            self.hour = "*/1"
            self.day_of_month = "*"
            self.month = "*"
            self.day_of_week = "*"
        elif schedule == WEEKLY_SUNDAY:
            self.minute = "0"
            self.hour = "0"
            self.day_of_month = "*"
            self.month = "*"
            self.day_of_week = "0"
    def set_custom_expression(self, expression):
        # Add validation logic for custom expression if necessary
        self.custom_expression = expression
    def get_expression(self):
        if self.custom_expression:
            return self.custom_expression
        return f"{self.minute} {self.hour} {self.day_of_month} {self.month} {self.day_of_week}"