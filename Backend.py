def read_database():
    with open('words.txt', 'r') as database:
        words =[word.strip() for word in database.readlines()]
        

