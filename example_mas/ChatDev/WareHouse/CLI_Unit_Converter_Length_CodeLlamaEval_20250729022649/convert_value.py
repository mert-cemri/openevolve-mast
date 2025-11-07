def convert_value(value, source_unit, target_unit):
    # Implement conversion logic here
    if source_unit == "meters" and target_unit == "feet":
        return value * 3.28084
    elif source_unit == "feet" and target_unit == "meters":
        return value / 3.28084
    else:
        raise ValueError("Invalid unit")