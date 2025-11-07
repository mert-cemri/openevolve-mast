import convert
def main():
    value = input("Enter a value: ")
    source_unit = input("Enter the source unit: ")
    target_unit = input("Enter the target unit: ")
    converted_value = convert.convert(value, source_unit, target_unit)
    print(f"{value} {source_unit} is equal to {converted_value} {target_unit}")
if __name__ == "__main__":
    main()