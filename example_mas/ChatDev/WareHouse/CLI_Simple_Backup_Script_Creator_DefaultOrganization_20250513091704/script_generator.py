'''
Contains functions to generate backup scripts using rsync and tar.
'''
def create_rsync_script(sources, target):
    script_lines = ["#!/bin/bash\n"]
    for source in sources:
        script_lines.append(f"rsync -av --progress {source} {target}\n")
    return ''.join(script_lines)
def create_tar_script(sources, target):
    script_lines = ["#!/bin/bash\n"]
    for source in sources:
        source_name = source.rstrip('/').split('/')[-1]
        script_lines.append(f"tar -cvf {target}/{source_name}.tar {source}\n")
    return ''.join(script_lines)