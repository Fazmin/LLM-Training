import re

class SimpleTokenizer:
    def __init__(self, split_char=' ', remove_punctuation=True, to_lower=True):

        self.split_char = split_char
        self.remove_punctuation = remove_punctuation
        self.to_lower = to_lower

    def tokenize(self, text):

        if self.to_lower:
            text = text.lower()
            
        if self.remove_punctuation:
            text = re.sub(r'[^\w\s]', '', text)

        tokens = text.split(self.split_char)

        return tokens

    def tokenize_file(self, file_path):

        tokens = []

        with open(file_path, 'r') as file:
            for line in file:
                tokens.append(self.tokenize(line))

        return tokens

tokenizer = SimpleTokenizer(split_char=' ', remove_punctuation=True, to_lower=True)

tokens = tokenizer.tokenize_file('full path to your file')
print(tokens)

