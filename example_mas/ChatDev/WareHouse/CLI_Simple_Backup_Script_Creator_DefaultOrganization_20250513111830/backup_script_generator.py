'''
Contains functions to generate backup scripts using rsync and tar.
'''
def generate_rsync_script(source_dirs, target_dir):
    '''
    Generates a shell script using rsync for backing up the specified source directories to the target directory.
    :param source_dirs: List of source directories to back up.
    :param target_dir: Target directory for the backup.
    :return: A string containing the shell script.
    '''
    script_lines = ["#!/bin/bash\n"]
    for source in source_dirs:
        script_lines.append(f"rsync -av --progress '{source}' '{target_dir}'\n")
    return ''.join(script_lines)
def generate_tar_script(source_dirs, target_dir):
    '''
    Generates a shell script using tar for backing up the specified source directories to the target directory.
    :param source_dirs: List of source directories to back up.
    :param target_dir: Target directory for the backup.
    :return: A string containing the shell script.
    '''
    script_lines = ["#!/bin/bash\n"]
    for source in source_dirs:
        base_name = source.rstrip('/').split('/')[-1]
        script_lines.append(f"tar -czvf '{target_dir}/{base_name}.tar.gz' -C '{source}' .\n")
    return ''.join(script_lines)