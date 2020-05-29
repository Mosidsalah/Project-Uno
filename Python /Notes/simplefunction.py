def yell_this():
    print('YOO')

yell_this()

def say_this(phrase):
    print(phrase)
say_this('Hello')
    
def yell_this(phrase):
    print(phrase.upper() + (' BRUH'))

yell_this('good morning')

words_to_yell = input()

def shout_this(phrase):
    print(phrase)
shout_this(words_to_yell.upper())

def make_doctor(name):
    full_name = name
    return full_name

print(make_doctor('Joe'))

def big_bubble(phrase):
    bubble = phrase + 'BRO' + phrase
    return bubble

bigger_bubble = big_bubble('BUBBLES')
print(bigger_bubble)

def make_schedule(period1,period2,period3):
    schedule = ('1st: '+ period1 + ' 2nd: ' + period2 + ' 3rd: ' + period3)
    return schedule

student_schedule = make_schedule('Math', 'Science', 'History')
print('SCHEDULE:',student_schedule)

def hat_available(color):
    hat_colors = 'black, green, orange, red'
    return(color.upper() in hat_colors.upper())

have_hat = hat_available('orange')
print(have_hat)

bird_suggestion = input('Enter a bird: ')

def bird_available():
    bird_types = 'crow, robin, pigeon'
    return(bird_suggestion.lower() in bird_types)

birdy_thingy = bird_available()
print('the',bird_suggestion, 'is', birdy_thingy)

def how_many():
    requested = input('enter how many: ')
    return(requested)
number_needed = how_many()
print(number_needed,'will be ordered')

def short_rhyme():
    print ('La la la')
    print ('Ba, ba, ba')

short_rhyme()

def title_it():
    message = 'msg'
    print(message.title())

title_it()
    
title_name = input('what is the title?')

def title_it():
    print(title_name)

title_it()
    
title_name = input('what is the title?')

def title_it_return():
    print(title_name.title())

title_it_return()
    
def bookstore(book,price):
    book_details = (book.title(),price)
    return book_details

book_entry = input('name a book: ')
price_entry = input('name a price: ')
book_stuff = bookstore(book_entry, price_entry)
print('Title:',book_stuff)


fish_entry = input('Fish: ')
price_entry = input('Price: ') 

def fishstore(fish,price):
    fishy = ('Fish type:' + fish_entry +',' + 'costs '+ price_entry)
    return fishy
fish_thing = fishstore(fish_entry,price_entry)
print(fish_thing)
