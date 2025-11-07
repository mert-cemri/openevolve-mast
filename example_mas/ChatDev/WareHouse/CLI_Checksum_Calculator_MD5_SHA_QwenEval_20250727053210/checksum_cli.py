'''
ChecksumCLI class to handle the command-line interface for the Checksum Utility.
'''
from checksum_calculator import ChecksumCalculator
class ChecksumCLI:
    def run(self, file_path):
        """Run the CLI interface and display checksums."""
        try:
            calculator = ChecksumCalculator()
            md5_checksum = calculator.calculate_md5(file_path)
            sha256_checksum = calculator.calculate_sha256(file_path)
            print(f"MD5: {md5_checksum}")
            print(f"SHA256: {sha256_checksum}")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except PermissionError:
            print(f"Error: Permission denied when accessing the file '{file_path}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")