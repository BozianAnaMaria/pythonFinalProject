
from selenium import webdriver

from urllib.request import urlopen
import bs4
import requests
from bs4 import BeautifulSoup


def get_url(url):
    goodreads_url = 'https://www.goodreads.com/'
    if not goodreads_url:
        print(input('try again: '))
    else:
        return 'correct'


def get_id(bookid):
    pattern = requests.compile("([^.-]+)")
    return pattern.search(bookid).group()


def book_description(url):
    data = urlopen(url)
    soup = BeautifulSoup(data, "html.parser")
    book_title = soup.find('h1', attrs={'class': 'Text Text__title1'}).text
    book_rating = soup.find('div', attrs={'class': 'RatingStatistics__rating'}).text
    book_author = soup.find('span', attrs={'class': 'ContributorLink__name'}).text
    book_title_sent = f'The title of the book is {book_title}'
    book_author_sent = f'The author of the book is {book_author}'
    book_rating_sent = f'The rating of this book is {book_rating}'
    return book_title_sent, book_author_sent, book_rating_sent


def book_back_cover(url):
    data = urlopen(url)
    soup = BeautifulSoup(data, "html.parser")
    book_back_cover_text = soup.find('div', attrs={'class': 'TruncatedContent__text TruncatedContent__text--large'}).text
    book_back_cover_sent = f'The description of this book is: {book_back_cover_text}'
    return book_back_cover_sent


def book_genres(url):
    global genres_sent
    data = urlopen(url)
    soup = BeautifulSoup(data, "html.parser")
    genres = []
    for genre in soup.find('span', attrs={'class': 'BookPageMetadataSection__genreButton'}).text.split():
        genres.append(genre)
        genres_sent = f'The main genre of this book is: {genres}'
    return genres_sent

#la fel arata none, chiar si daca prima data cand am dat run la functie pai mergea far probleme
def people_reading(book_code):
    url = book_code
    driver = webdriver.Chrome()
    driver.get(url)
    stat = driver.find_elements_by_xpath('//div[@class="SocialSignalsSection__caption"]').text
    return stat


def publish(url):
    global book_f_sent
    data = urlopen(url)
    soup = BeautifulSoup(data, "html.parser")
    book_feature = soup.find('div', attrs={'class': 'FeaturedDetails'}).text.split()
    book_f_sent = f'This book was published on {book_feature[4],book_feature[5],book_feature[6]}'
    return book_f_sent

#code cu problema
def book_ex(book_code):
    url = book_code
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(3)
    book_1_ex = driver.find_elements_by_xpath('//div[@class="BookCard__title"]')
    author_1_ex = driver.find_elements_by_xpath('//div[@class="BookCard__authorName"]')
    rating_1_ex = driver.find_elements_by_xpath('//span[@class="Text Text__body3 Text__semi-bold Text__body-standard"]')

    book_1_list = []
    author_1_list = []
    rating_1_list = []

    for el in book_1_ex:
        book_1_list.append(el.text)
        driver.implicitly_wait(3)

    for el in range(3):
        author_1_list.append(author_1_ex[el].text)

    for el in range(3):
        rating_1_list.append(rating_1_ex[el].text)

    book_1_sent = f'Many enjoyed {book_1_ex} writen by {author_1_list}. Its rating is: {rating_1_list}'
    return book_1_sent


#alta problema
#varianta care merge
def get_reviewer_name(url):
    data = urlopen(url)
    soup = BeautifulSoup(data, "html.parser")
    review_name = soup.find('div', attrs={'class': 'ReviewerProfile__name'}).text
    review_info = soup.find('section', attrs={'class': 'ReviewText__content'}).text
    return f'This is what {review_name} thinks about this book: {review_info}'

#varianta care nu merge
def get_reviewer_name_1(book_code):
    url = book_code
    driver = webdriver.Chrome()
    driver.get(url)

    review_name_1_list = []
    review_info_1_list = []

    review_name_1 = driver.find_elements_by_xpath('//div[@class="ReviewerProfile__name"]')
    review_info_1 = driver.find_elements_by_xpath('//section[@class="ReviewText__content"]')

    for el in range(len(review_name_1)):
        review_name_1_list.append(review_name_1[el].text)

    for el in range(len(review_info_1)):
        review_info_1_list.append(review_info_1[el].text)

    return f'This is what {review_name_1_list} thinks about this book: {review_info_1_list}'


def book_intro(book_code):
    url = book_code
    source = urlopen(url)
    soup = bs4.BeautifulSoup(source, "html.parser")

    book_book = ({
        'book_1': book_description(url),
        'book_2': book_back_cover(url),
        'book_3': book_genres(url),
        #'book_4': people_reading(url), 
        'book_5': publish(url),
        'book_6': get_reviewer_name(url)
    })
    return book_book


def get_book_url(book_code):
    url = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url)

    if not source:
        return 'nothing'
    else:
        return 'found something', book_ex(url)



gr_url_code = input('goodreads url: ')
print(get_url(gr_url_code))
search_text = input('what book are you looking for? Insert book code: ')
print(get_book_url(search_text))
