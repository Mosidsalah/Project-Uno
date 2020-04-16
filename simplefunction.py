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

    
