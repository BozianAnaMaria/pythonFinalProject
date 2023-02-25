from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_webdriver():
    service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    return driver


def get_url(url_1):
    goodreads_url = 'https://www.goodreads.com/'
    if not goodreads_url:
        print(input('try again: '))
    else:
        return 'correct'


def book_description(book_code):
    url_1 = book_code
    driver = get_webdriver()
    driver.get(url_1)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//h1[@class="Text Text__title1"]')))
    book_title = driver.find_elements(By.XPATH, '//h1[@class="Text Text__title1"]')
    book_rating = driver.find_elements(By.XPATH, '//div[@class="RatingStatistics__rating"]')
    book_author = driver.find_elements(By.XPATH, '//span[@class="ContributorLink__name"]')

    book_t_ = [a.text for a in book_title]
    book_a_ = [a.text for a in book_author]
    book_r_ = [a.text for a in book_rating]

    book_title_sent = f'The title of the book is {book_t_[0]}'
    book_author_sent = f'The author of the book is {book_a_[0]}'
    book_rating_sent = f'The rating of this book is {book_r_[0]}'

    driver.close()
    return {
        '1': book_title_sent,
        '2': book_author_sent,
        '3': book_rating_sent
    }


def book_back_cover(url_1):
    data = urlopen(url_1)
    soup = BeautifulSoup(data, "html.parser")
    book_back_cover_text = soup.find('div', attrs={'class': 'TruncatedContent__text TruncatedContent__text--large'}).text
    book_back_cover_sent = f'The description of this book is: {book_back_cover_text}'
    return book_back_cover_sent


def book_genres(book_code):
    url_1 = book_code
    driver = get_webdriver()
    driver.get(url_1)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//span[@class="BookPageMetadataSection__genreButton"]')))
    genres_loc = driver.find_elements(By.XPATH, '//span[@class="BookPageMetadataSection__genreButton"]')

    genre_loc_1 = [a.text for a in genres_loc]

    genres = []
    for genre in genre_loc_1:
        genres.append(genre)

    genres_stat = f'The main genres of this book are: {genres}'

    driver.close()
    return genres_stat


def people_reading(book_code):
    url_1 = book_code
    driver = get_webdriver()
    driver.get(url_1)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="SocialSignalsSection__caption"]')))
    stat = driver.find_elements(By.XPATH, '//div[@class="SocialSignalsSection__caption"]')

    stat_1 = [a.text for a in stat]

    driver.close()
    return stat_1


def publish(book_code):
    url_1 = book_code
    driver = get_webdriver()
    driver.get(url_1)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="FeaturedDetails"]')))
    book_feature = driver.find_elements(By.XPATH, '//div[@class="FeaturedDetails"]')

    book_feat = [a.text.split(' ', 4) for a in book_feature]
    book_f = book_feat[-1]

    book_f_sent = f'This book was published on {book_f[-1]}'

    driver.close()
    return book_f_sent


def book_ex(book_code):
    url_1 = book_code
    driver = get_webdriver()
    driver.get(url_1)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="BookCard__title"]')))
    book_1_ex = driver.find_elements(By.XPATH, '//div[@class="BookCard__title"]')
    author_1_ex = driver.find_elements(By.XPATH, '//div[@class="BookCard__authorName"]')

    books = [a.text for a in book_1_ex]
    authors = [a.text for a in author_1_ex]

    recommendations = []
    for book, author, rating in zip(books, authors, range(len(books))):
        recommendations.append(
            f'Many enjoyed {book} writen by {author}.'
        )

    driver.close()
    return recommendations


def get_reviewer_name(url_1):
    data = urlopen(url_1)
    soup = BeautifulSoup(data, "html.parser")
    review_name = soup.find('div', attrs={'class': 'ReviewerProfile__name'}).text
    review_info = soup.find('section', attrs={'class': 'ReviewText__content'}).text
    return f'This is what {review_name} thinks about this book: {review_info}'


def get_reviewer_name_1(book_code):
    url_1 = book_code
    driver = get_webdriver()
    driver.get(url_1)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="ReviewerProfile__name"]')))
    review_name_1 = driver.find_elements(By.XPATH, '//div[@class="ReviewerProfile__name"]')
    review_info_1 = driver.find_elements(By.XPATH, '//section[@class="ReviewText__content"]')

    rev_name = [a.text for a in review_name_1]
    rev_info = [a.text for a in review_info_1]

    reviews = []
    for name, info, rating in zip(rev_name, rev_info, range(5)):
        reviews.append(
            f'This is what {name} thinks about this book: {info}'
        )

    driver.close()
    return reviews


def book_intro(book_code):
    url_1 = book_code
    source = urlopen(url_1)
    soup = BeautifulSoup(source, "html.parser")

    book_book = ({
        'book_1': book_description(url_1),
        'book_2': book_back_cover(url_1),
        'book_3': book_genres(url_1),
        'book_4': publish(url_1),
        'book_5': book_ex(url_1),
        'book_6': get_reviewer_name_1(url_1)
    })
    return book_book


def get_book_url(book_code):
    url_1 = 'https://www.goodreads.com/book/show/' + book_code
    source = requests.get(url_1)

    if not source:
        return 'nothing'
    else:
        return 'found something', book_ex(url_1)


if __name__ == '__main__':
    gr_url_code = input('goodreads url: ')
    print(get_url(gr_url_code))
    search_text = input('what book are you looking for? Insert book code: ')
    url = get_book_url(search_text)
    print(url)
