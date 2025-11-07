'''
Utility class for converting time strings into seconds.
'''
class TimeConverter:
    @staticmethod
    def convert_to_seconds(time_str):
        total_seconds = 0
        time_units = {'h': 3600, 'm': 60, 's': 1}
        num = ''
        for char in time_str:
            if char.isdigit():
                num += char
            elif char in time_units:
                total_seconds += int(num) * time_units[char]
                num = ''
        # Add remaining number as seconds if no unit is specified
        if num:
            total_seconds += int(num)
        return total_seconds