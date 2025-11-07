import os
class Splitter:
    '''
    Split a large file into smaller parts.
    '''
    def __init__(self, input_file, output_dir, size):
        self.input_file = input_file
        self.output_dir = output_dir
        self.size = size
    def split(self):
        '''
        Split the input file into smaller parts.
        '''
        with open(self.input_file, 'rb') as f:
            data = f.read()
        parts = []
        while data:
            part = data[:self.size]
            parts.append(part)
            data = data[self.size:]
        for i, part in enumerate(parts):
            output_file = os.path.join(self.output_dir, f'part{i}.txt')
            with open(output_file, 'wb') as f:
                f.write(part)