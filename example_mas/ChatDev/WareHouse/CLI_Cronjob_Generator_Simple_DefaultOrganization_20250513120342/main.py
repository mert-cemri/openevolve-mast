'''
Main application file for the CLI cronjob generator.
'''
import argparse
from cron_expression_generator import CronExpressionGenerator
def main():
    '''
    Main function to handle CLI interactions and generate cron expressions.
    '''
    parser = argparse.ArgumentParser(description='CLI Cronjob Generator')
    parser.add_argument('schedule', choices=['daily_3am', 'every_15_minutes', 'hourly', 'weekly'],
                        help='Select a schedule: daily_3am, every_15_minutes, hourly, weekly')
    args = parser.parse_args()
    cron_expression = CronExpressionGenerator.generate_expression(args.schedule)
    print(f"Cron Expression: {cron_expression}")
if __name__ == "__main__":
    main()