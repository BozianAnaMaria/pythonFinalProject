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
        ans = input('Try again: ')
        print(ans)
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


def get_book_description(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_4 = input('1. Would you like to see BOOK DESCRIPTION? ').lower()
    print(answer_4)
    while answer_4:
        if answer_4 == 'yes':
            b_descr = book_description(url_1)
            print(b_descr)
            with open('BOOK-DESCRIPTION.json', 'w+') as file:
                json_data = json.dumps(b_descr)
                file.write(json_data)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return get_back_cover(url_2)

        if answer_4 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return get_back_cover(url_2)
        else:
            try:
                error_text = 'Input should be "yes" or "no": '
                print(error_text)
                return get_book_description(book_code)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def get_back_cover(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_5 = input('2. Would you like to see the BACK COVER of the book? ').lower()
    print(answer_5)

    while answer_5:
        if answer_5 == 'yes':
            b_back_cov = book_back_cover(url_1)
            print(b_back_cov)
            with open('BOOK-BACK-COVER.json', 'w+') as file:
                json_data = json.dumps(b_back_cov)
                file.write(json_data)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return get_book_genres(url_2)

        if answer_5 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return get_book_genres(url_2)
        else:
            try:
                error_text = 'Input should be "yes" or "no": '
                print(error_text)
                return get_back_cover(book_code)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def get_book_genres(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_6 = input('3. Would you like to see the GENRES of the book? ').lower()
    print(answer_6)

    while answer_6:
        if answer_6 == 'yes':
            b_gen = book_genres(url_1)
            print(b_gen)
            with open('BOOK-GENRES.json', 'w+') as file:
                json_data = json.dumps(b_gen)
                file.write(json_data)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return get_publish_date(url_2)

        if answer_6 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return get_publish_date(url_2)
        else:
            try:
                error_text = 'Input should be "yes" or "no": '
                print(error_text)
                return get_book_genres(book_code)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def get_publish_date(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_7 = input('4. Would you like to see when it was PUBLISHED? ').lower()
    print(answer_7)

    while answer_7:
        if answer_7 == 'yes':
            b_pub = publish(url_1)
            print(b_pub)
            with open('BOOK-DATE.json', 'w+') as file:
                json_data = json.dumps(b_pub)
                file.write(json_data)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return get_book_statistic(url_2)

        if answer_7 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return get_book_statistic(url_2)
        else:
            try:
                error_text = 'Input should be "yes" or "no": '
                print(error_text)
                return get_publish_date(book_code)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def get_book_statistic(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_8 = input('5. Would you like to see the STATISTICS for this book? ')
    print(answer_8)

    while answer_8:
        if answer_8 == 'yes':
            b_stat = people_reading(url_1)
            print(b_stat)
            with open('BOOK-STATISTICS.json', 'w+') as file:
                json_data = json.dumps(b_stat)
                file.write(json_data)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return get_similar_books(url_2)

        if answer_8 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return get_similar_books(url_2)
        else:
            try:
                error_text = 'Input should be "yes" or "no": '
                print(error_text)
                return get_book_statistic(book_code)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def get_similar_books(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_11 = input('6. Would you like to see SIMILAR BOOKS? ').lower()
    print(answer_11)

    while answer_11:
        if answer_11 == 'yes':
            b_sim = book_ex(url_1)
            print(b_sim)
            with open('SIMILAR-BOOKS.json', 'w+') as file:
                json_data = json.dumps(b_sim)
                file.write(json_data)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return get_book_reviews(url_2)

        if answer_11 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return get_book_reviews(url_2)
        else:
            try:
                error_text = 'Input should be "yes" or "no": '
                print(error_text)
                return get_similar_books(book_code)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def get_book_reviews(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_9 = input('7. Would you like to see REVIEWS for this book? ').lower()
    print(answer_9)

    while answer_9:
        if answer_9 == 'yes':
            b_rev = get_reviewer_name_1(url_1)
            print(b_rev)
            with open('REVIEWS.json', 'w+') as file:
                json_data = json.dumps(b_rev)
                file.write(json_data)
                answer_11 = '\nTo see all that you have selected, look through the different JSON files.\n '
                print(answer_11)
                time.sleep(5)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return add_want_to_read(url_2)

        if answer_9 == 'no':
            answer_11 = '\nTo see all that you have selected, look through the different JSON files.\n '
            print(answer_11)
            time.sleep(5)
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return add_want_to_read(url_2)
        else:
            try:
                error_text = 'Input should be "yes" or "no": '
                print(error_text)
                return get_book_reviews(book_code)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def add_want_to_read(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_10 = input('8. Would you like to add this book to WANT TO READ or MOVE TO THE NEXT ONE? \n'
                      '(variants of answer: "read" or "move")\n').lower()
    while answer_10:
        if answer_10 == 'read':
            with open('WANT-TO-READ.json', 'w+') as file:
                json_data = json.dumps(book_description(url_1))
                file.write(json_data)
                url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
                return get_diff_book(url_2)

        if answer_10 == 'move':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return get_diff_book(url_2)

        else:
            try:
                error_text = 'Input should be "read" or "move" '
                print(error_text)
                return add_want_to_read(book_code)
            except:
                DecideReadOrMove('Input should be "read" or "move" ')
        break


def get_diff_book(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)
    answer_12 = input('9. Would you like to search a DIFFERENT book? \n'
                      'Answer with "yes" or "no" ').lower()
    print(answer_12)

    while answer_12:
        if answer_12 == 'yes':
            answer_ = input(
                '\nNext, will appear one question at a time. PLEASE, answer with "yes" or "no".\n'
                'To finish, you have to answer to all of them. \n'
                'If you do not answer properly, the question will reappear.\n '
                '\nPlease, enter a different BOOK CODE: ')
            get_book_url(answer_)
            return get_book_description(answer_)

        elif answer_12 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return ready_to_stop(url_2)
        else:
            try:
                error_text = 'Input should be "yes" or "no": '
                print(error_text)
                return get_diff_book(book_code)
            except:
                InputTEXTError('Input should be yes or no: ')
        break


def ready_to_stop(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    answer_13 = input('10. Are you sure you want to stop? ').lower()
    while answer_13:
        if answer_13 != 'yes' != 'no':
            try:
                error_text = 'Input should be "yes" or "no": '
                print(error_text)
                return ready_to_stop(book_code)
            except:
                InputTEXTError('Input should be yes or no: ')
        if answer_13 == 'no':
            url_2 = url_1.split('https://www.goodreads.com/book/show/')[-1]
            return get_diff_book(url_2)
        if answer_13 == 'yes':
            print('You have finished.')
            break
        break
    breakpoint()


def all_info(book_code):
    url_1 = book_code

    return {
        '1': get_book_description(url_1),
        '2': get_back_cover(url_1),
        '3': get_book_genres(url_1),
        '4': get_publish_date(url_1),
        '5': get_book_statistic(url_1),
        '6': get_similar_books(url_1),
        '7': get_book_reviews(url_1),
        '8': add_want_to_read(url_1)
    }


answer = input('\nNext, will appear one question at a time, in this order. PLEASE, answer with "yes" or "no".\n'
               'To finish, you have to answer to all of them. \n'
               'If you do not answer properly, the question will reappear. \n'
               '\nPlease, enter BOOK CODE again: ')
print(all_info(answer))
