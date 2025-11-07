'''
Main file to run the checksum calculator application as a CLI utility.
'''
import argparse
from checksum_calculator import ChecksumCalculator
def main():
    parser = argparse.ArgumentParser(description='Calculate MD5 and SHA256 checksums of a file.')
    parser.add_argument('file_path', type=str, help='Path to the file for which to calculate checksums.')
    args = parser.parse_args()
    calculator = ChecksumCalculator()
    try:
        md5_checksum = calculator.calculate_md5(args.file_path)
        sha256_checksum = calculator.calculate_sha256(args.file_path)
        print(f"MD5: {md5_checksum}")
        print(f"SHA256: {sha256_checksum}")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()