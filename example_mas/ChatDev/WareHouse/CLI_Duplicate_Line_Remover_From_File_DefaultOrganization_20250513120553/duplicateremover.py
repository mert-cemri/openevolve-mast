class DuplicateRemover:
    def remove_duplicates(self, file_path):
        seen = set()
        result = []
        with open(file_path, 'r') as file:
            for line in file:
                if line not in seen:
                    seen.add(line)
                    result.append(line)
        return ''.join(result)