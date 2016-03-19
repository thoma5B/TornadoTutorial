# tornado-sqlalchemy/test/__main__.py
#
# run through
#     python -m unittest tests.test_session


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


import model


def session():

	engine = create_engine('sqlite:///:memory:', echo=True)
	Session = sessionmaker(bind=engine)
	#Session = sessionmaker()
	# Session.configure(bind=engine)

	lorem_page = model.Page(content='Lorem Ipsum', heading='Ed Jones')

	assert lorem_page.content == 'Lorem Ipsum'
	assert lorem_page.heading == 'Ed Jones'
	assert lorem_page.id == 1, 'lorem_page.id should be {} but is {} instead'.format(1, lorem_page.id)

session()