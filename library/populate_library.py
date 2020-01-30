import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','library.settings')

import django
# Import settings
django.setup()

import random
from libraryMontevideo.models import Book,Author
from faker import Faker

fakegen = Faker()
topics = ['Adventure','Social','Criminal','Romance','Games']

def add_topic():
    t = topics[fakegen.random_int(min=0, max=4, step=1)]
    return t



def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):
        # Create Authors
        name = fakegen.name()
        is_female = fakegen.pybool()
        ocupation = fakegen.job()
        email = fakegen.ascii_company_email()

        author  = Author.objects.get_or_create(name=name,is_female=is_female,ocupation=ocupation,email=email)[0]

        for entry in range(fakegen.random_int(min=2, max=7, step=1)):
            # Create Books
            top = add_topic()
            date = fakegen.date()
            name = fakegen.paragraph(nb_sentences=1, variable_nb_sentences=True, ext_word_list=None)
            pages = fakegen.random_int(min=200, max=700, step=1)
            book = Book.objects.get_or_create(date=date,topic=top,pages=pages)[0]
            book.author.add(author)


def update_books():
    for book in Book.objects.all():
        book.name = fakegen.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        book.save();

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    #populate(20)
    update_books()
    print('Populating Complete')
