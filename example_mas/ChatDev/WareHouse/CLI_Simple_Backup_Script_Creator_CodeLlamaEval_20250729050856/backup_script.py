import os
import sys
def create_backup_script(source_dirs, target_dir):
    # Create a new script file
    script_file = open("backup_script.sh", "w")
    # Write the script header
    script_file.write("#!/bin/bash\n")
    # Write the source directories
    for source_dir in source_dirs:
        script_file.write("rsync -avz --delete {} {}/{}\n".format(source_dir, target_dir, os.path.basename(source_dir)))
    # Write the target directory
    script_file.write("rsync -avz --delete {} {}\n".format(target_dir, os.path.basename(target_dir)))
    # Close the script file
    script_file.close()
    # Make the script executable
    os.chmod("backup_script.sh", 0o755)
    # Print a success message
    print("Backup script created successfully!")