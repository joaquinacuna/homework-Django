import os
# Configure settings for project
# Need to run this before calling models from application!

os.environ.setdefault('DJANGO_SETTINGS_MODULE','libraryMontevideo.settings')

import django
# Import settings
django.setup()

import random
from libraryMontevideo.models import Book,Author
from faker import Faker

fakegen = Faker()
topics = ['Adventure','Social','Criminal','Romance','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t



def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):
        # Create Authors
        name = fakegen.name()
        is_female = fake.pybool()
        ocupation = fake.job()
        email = fake.ascii_company_email(*args, **kwargs)

        author  = Author.objects.get_or_create(name=name,is_female=is_female,ocupation=ocupation,email=email)[0]

        for entry in range(fake.random_int(min=2, max=7, step=1)):
            # Create Books
            top = add_topic()
            date = fakegen.date()
            name = fakegen.fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
            pages = fake.profile(fields=None, sex=None)
            book = Book.objects.get_or_create(author=author,date=fake_date,topic=top,pages=pages)[0]
