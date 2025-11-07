import sys
# Get the source directories and target directory from the command line arguments
source_dirs = sys.argv[1:]
target_dir = sys.argv[0]
# Create the backup script
from backup_script import create_backup_script
create_backup_script(source_dirs, target_dir)