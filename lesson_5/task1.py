with open('text.txt', 'w') as f:
    while True:
        text = input('')
        f.write(text + '\n')
        if not text:
            break

