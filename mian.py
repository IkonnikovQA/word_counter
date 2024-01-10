text = input('enter text: ')

words = text.split()
sentences = text.split('.')

def print_stat(words_count=0, letters_count=0, sentences_count=0):
    if words_count:
        if words_count == 1:
            print(f'there is only one word in the text')
        else:
            print(f'word count: {words_count}')
    if letters_count:
        print(f'number of offers: {letters_count}')
    if sentences_count:
        print(f'number of offers: {sentences_count}')


print_stat(words_count=len(words), letters_count=len(text), sentences_count=len(sentences) - 1)

