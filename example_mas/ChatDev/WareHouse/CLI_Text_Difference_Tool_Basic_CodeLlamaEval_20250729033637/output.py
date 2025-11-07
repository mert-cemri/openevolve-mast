import os
def write_output(diff, output_file):
    with open(output_file, "w") as f:
        f.write(diff)
    return True