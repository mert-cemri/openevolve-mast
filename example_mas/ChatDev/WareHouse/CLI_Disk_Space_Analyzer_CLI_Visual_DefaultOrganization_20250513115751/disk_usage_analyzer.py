'''
Disk usage analyzer class to calculate and report disk usage statistics.
'''
from file_system_utils import FileSystemUtils
import os
class DiskUsageAnalyzer:
    def __init__(self, directory):
        self.directory = directory
    def get_disk_usage_report(self):
        usage_data = FileSystemUtils.get_directory_size(self.directory)
        sorted_usage = sorted(usage_data.items(), key=lambda item: item[1], reverse=True)
        report_lines = []
        for path, size in sorted_usage:
            # Calculate the indentation level based on the directory depth
            indent_level = path.count(os.sep) - self.directory.count(os.sep)
            indent = ' ' * (indent_level * 4)  # 4 spaces per level of depth
            report_lines.append(f"{indent}{os.path.basename(path)}: {size} bytes")
        report_lines.append(f"\nTotal files processed: {len(usage_data)}")
        return "\n".join(report_lines)