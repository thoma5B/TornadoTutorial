from sqlalchemy import orm
import datetime
from sqlalchemy import schema, types

metadata = schema.MetaData()



def now():
    return datetime.datetime.now()

# page_table = schema.Table('page', metadata,
#     schema.Column('id', types.Integer,
#         schema.Sequence('page_seq_id', optional=True), primary_key=True),
#     schema.Column('content', types.Text(), nullable=False),
#     schema.Column('posted', types.DateTime(), default=now),
#     schema.Column('title', types.Unicode(255), default=u'Untitled Page'),
#     schema.Column('heading', types.Unicode(255)),
# )
# comment_table = schema.Table('comment', metadata,
#     schema.Column('id', types.Integer,
#         schema.Sequence('comment_seq_id', optional=True), primary_key=True),
#     schema.Column('pageid', types.Integer,
#         schema.ForeignKey('page.id'), nullable=False),
#     schema.Column('content', types.Text(), default=u''),
#     schema.Column('name', types.Unicode(255)),
#     schema.Column('email', types.Unicode(255), nullable=False),
#     schema.Column('created', types.TIMESTAMP(), default=now()),
# )
# pagetag_table = schema.Table('pagetag', metadata,
#     schema.Column('id', types.Integer,
#         schema.Sequence('pagetag_seq_id', optional=True), primary_key=True),
#     schema.Column('pageid', types.Integer, schema.ForeignKey('page.id')),
#     schema.Column('tagid', types.Integer, schema.ForeignKey('tag.id')),
# )
# tag_table = schema.Table('tag', metadata,
#     schema.Column('id', types.Integer,
#         schema.Sequence('tag_seq_id', optional=True), primary_key=True),
#     schema.Column('name', types.Unicode(20), nullable=False, unique=True),
# )



# orm.mapper(Page, page_table, properties={
#     'comments':orm.relation(Comment, backref='page'),
#     'tags':orm.relation(Tag, secondary=pagetag_table)
# })
# orm.mapper(Comment, comment_table)
# orm.mapper(Tag, tag_table)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Unicode, DateTime, TIMESTAMP, Text  # types.[]
from sqlalchemy.schema import Sequence, ForeignKey #schema.sequence

from settings import *

logger = init_logging_mode(__name__)

Base = declarative_base()

# Integer = lambda *args, **kwargs: Column(Integer, *args, **kwargs)

class Page(Base):
    __tablename__ = 'page'
    id = Column(
        Integer,
        Sequence('page_seq_id', optional=True),
        primary_key=True,
        )
    content = Column(Text(), nullable=False)
    posted = Column(DateTime(), default=now)
    title = Column(Unicode(255), default=u'Untitled Page')
    heading = Column(Unicode(255))


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(
        Integer, 
        Sequence('comment_seq_id', optional=True), 
        primary_key=True,
        )
    pageid = Column(Integer, schema.ForeignKey('page.id'), nullable=False)
    content = Column(Text(), default=u'')
    name = Column(Unicode(255), nullable=False, unique=True)
    email = Column(Unicode(255), nullable=False)
    created = Column(TIMESTAMP(), default=now())


class Page_Tag(Base):
    __tablename__ = 'pagetag' 
    id = Column(
        Integer, 
        Sequence('pagetag_seq_id', optional=True), 
        primary_key=True,
        )
    pageid = Column(Integer, ForeignKey('page.id'))
    tagid = Column(Integer, ForeignKey('tag.id'))


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(
        Integer, 
        Sequence('tag_seq_id', optional=True), 
        primary_key=True,
        )
    name = Column(Unicode(20), nullable=False, unique=True)


# Base.metadata.create_all(engine)


# from sqlalchemy import create_engine

# # Create an engine and create all the tables we need
# engine = create_engine('sqlite:///:memory:', echo=True)
# metadata.bind = engine
# metadata.create_all()

# # Set up the session
# sm = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False,
#     expire_on_commit=True)
# session = orm.scoped_session(sm)
