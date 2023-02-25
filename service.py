import time
import requests
import json
from main import book_ex
from main import book_description
from main import book_back_cover
from main import book_genres
from main import publish
from main import get_reviewer_name_1
from main import people_reading


class InputTEXTError(Exception):
    pass


class DecideReadOrMove(Exception):
    pass


print('Hello there and welcome to Goodreads!\n'
      'In this program you can see descriptions of books, their back covers, main genre, similar options and '
      'reviews.\n'
      'To access information, all you will have to do is answer some questions.\n')

answer_1 = input('Are you ready? ')
print('Enjoy!\n\n')

print('First, you need to access Goodreads.')


def enter_gr_url(url):
    if url != 'https://www.goodreads.com/':
        print(input('Try again: '))
    else:
        print('Correct.')


answer_2 = input('Please, enter URL: ')
enter_gr_url(answer_2)


def get_book_url(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    if not source:
        print('Nothing')
    else:
        print('Found what you are looking for!')


answer_3 = input('What book are you looking for? Insert BOOK CODE: ')
get_book_url(answer_3)

options = {
    '1': 'BOOK-DESCRIPTION',
    '2': 'BOOK-BACK-COVER',
    '3': 'BOOK-GENRES',
    '4': 'PUBLISHED-DATE',
    '5': 'STATISTICS',
    '6': 'SIMILAR-BOOKS',
    '7': 'REVIEWS',
    '8': 'WANT TO READ'
}
print('\n\nHere are the options that you can see for this book:\n', options)


def new_fun(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_4 = (input('1. Would you like to see BOOK DESCRIPTION? '))
    print(answer_4)
    while answer_4:
        if answer_4 == 'yes':
            with open('BOOK-DESCRIPTION.json', 'w+') as file:
                json_data = json.dumps(book_description(url_1), )
                file.write(json_data)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return new_fun_2(url_2)

        if answer_4 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return new_fun_2(url_2)
        else:
            try:
                error_text = input('Input should be "yes" or "no": ')
                print(error_text)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def new_fun_2(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_5 = input('2. Would you like to see the BACK COVER of the book? ').lower()
    print(answer_5)

    while answer_5:
        if answer_5 == 'yes':
            with open('BOOK-BACK-COVER.json', 'w+') as file:
                json_data = json.dumps(book_back_cover(url_1), )
                file.write(json_data)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return new_fun_3(url_2)

        if answer_5 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return new_fun_3(url_2)
        else:
            try:
                error_text = input('Input should be "yes" or "no": ')
                print(error_text)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def new_fun_3(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_6 = input('3. Would you like to see the GENRES of the book? ').lower()
    print(answer_6)

    while answer_6:
        if answer_6 == 'yes':
            with open('BOOK-GENRES.json', 'w+') as file:
                json_data = json.dumps(book_genres(url_1), )
                file.write(json_data)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return new_fun_4(url_2)

        if answer_6 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return new_fun_4(url_2)
        else:
            try:
                error_text = input('Input should be "yes" or "no": ')
                print(error_text)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def new_fun_4(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_7 = input('4. Would you like to see when it was PUBLISHED? ').lower()
    print(answer_7)

    while answer_7:
        if answer_7 == 'yes':
            with open('BOOK-DATE.json', 'w+') as file:
                json_data = json.dumps(publish(url_1), )
                file.write(json_data)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return new_fun_5(url_2)

        if answer_7 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return new_fun_5(url_2)
        else:
            try:
                error_text = input('Input should be "yes" or "no": ')
                print(error_text)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def new_fun_5(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_8 = input('5. Would you like to see the STATISTICS for this book? ')
    print(answer_8)

    while answer_8:
        if answer_8 == 'yes':
            with open('BOOK-DATE.json', 'w+') as file:
                json_data = json.dumps(people_reading(url_1), )
                file.write(json_data)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return new_fun_6(url_2)

        if answer_8 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return new_fun_6(url_2)
        else:
            try:
                error_text = input('Input should be "yes" or "no": ')
                print(error_text)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def new_fun_6(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_11 = input('6. Would you like to see SIMILAR BOOKS? ').lower()
    print(answer_11)

    while answer_11:
        if answer_11 == 'yes':
            with open('SIMILAR-BOOKS.json', 'w+') as file:
                json_data = json.dumps(book_ex(url_1), )
                file.write(json_data)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return new_fun_7(url_2)

        if answer_11 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return new_fun_7(url_2)
        else:
            try:
                error_text = input('Input should be "yes" or "no": ')
                print(error_text)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def new_fun_7(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_9 = input('7. Would you like to see REVIEWS for this book? ').lower()
    print(answer_9)

    while answer_9:
        if answer_9 == 'yes':
            with open('REVIEWS.json', 'w') as file:
                json_data = json.dumps(get_reviewer_name_1(url_1), )
                file.write(json_data)
                answer_11 = '\nTo see all that you have selected, look the through different files.\n '
                print(answer_11)
                time.sleep(5)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return new_fun_8(url_2)

        if answer_9 == 'no':
            answer_11 = '\nTo see all that you have selected, look the through different files.\n '
            print(answer_11)
            time.sleep(5)
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return new_fun_8(url_2)
        else:
            try:
                error_text = input('Input should be "yes" or "no": ')
                print(error_text)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def new_fun_8(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_10 = input('8. Would you like to add this book to WANT TO READ or MOVE TO THE NEXT ONE or STOP? \n'
                       '(variants of answer: "read"/"move"/"stop")\n').lower()
    while answer_10:
        if answer_10 == 'read':
            with open('WANT-TO-READ.json', 'w+') as file:
                json_data = json.dumps(book_description(url_1), )
                file.write(json_data)

                inp_text = input('\nWould you like to SEARCH another book? \n'
                                     'Answer with "yes" or "no" ').lower()
                while inp_text:
                    if inp_text == 'yes':
                        answer_ = input(
                            '\nNext, will appear one question at a time. PLEASE, answer with "yes" or "no".\n'
                            'To finish, you have to answer to all of them. \n'
                            'If you do not answer properly, the question will reappear.\n '
                            '\nPlease, enter BOOK CODE again: ')
                        return new_fun_9(answer_)

                    elif inp_text == 'no':
                        print('Done')
                        break
                    else:
                        try:
                            error_text = input('Input should be "yes" or "no": ')
                            print(error_text)
                        except:
                            InputTEXTError('Input should be yes or no: ')
                break

        if answer_10 == 'stop':
            print('Done')
            break

        if answer_10 == 'move':
            answer_ = input(
                '\nNext, will appear one question at a time. PLEASE, answer with "yes" or "no".\n'
                'To finish, you have to answer to all of them. \n'
                'If you do not answer properly, the question will reappear.\n '
                '\nPlease, enter BOOK CODE again: ')
            return new_fun_9(answer_)

        if answer_10 != 'read' != 'move' != 'stop':
            try:
                error_text = input('Input should be "read"/"move"/"stop"')
                print(error_text)
            except:
                DecideReadOrMove('Input should be "read" or "move" or "stop" ')
        break


def new_fun_9(book_code):
    url_1 = book_code

    return {
        '1': new_fun(url_1),
        '2': new_fun_2(url_1),
        '3': new_fun_3(url_1),
        '4': new_fun_4(url_1),
        '5': new_fun_5(url_1),
        '6': new_fun_6(url_1),
        '7': new_fun_7(url_1),
        '8': new_fun_8(url_1)
    }


answer = input('\nNext, will appear one question at a time, in this order. PLEASE, answer with "yes" or "no".\n'
               'To finish, you have to answer to all of them. \n'
               'If you do not answer properly, the question will reappear. \n'
               '\nPlease, enter BOOK CODE again: ')
print(new_fun_9(answer))

