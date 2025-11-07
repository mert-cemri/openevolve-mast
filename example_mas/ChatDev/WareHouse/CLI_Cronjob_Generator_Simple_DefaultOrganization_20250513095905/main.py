'''
Main application file for the CLI cronjob generator.
'''
import argparse
from cron_expression import CronExpression, DAILY_3AM, EVERY_15_MINUTES, EVERY_HOUR, WEEKLY_SUNDAY
def main():
    parser = argparse.ArgumentParser(description="CLI Cronjob Generator")
    parser.add_argument(
        'schedule',
        choices=[DAILY_3AM, EVERY_15_MINUTES, EVERY_HOUR, WEEKLY_SUNDAY],
        help="Select a schedule: daily_3am, every_15_minutes, every_hour, weekly_sunday"
    )
    parser.add_argument(
        '--custom',
        type=str,
        help="Provide a custom cron expression"
    )
    args = parser.parse_args()
    cron_expression = CronExpression()
    if args.custom:
        cron_expression.set_custom_expression(args.custom)
    else:
        cron_expression.set_schedule(args.schedule)
    cron_line = cron_expression.get_expression()
    print(f"Cron Expression: {cron_line}")
if __name__ == "__main__":
    main()