from scrapy.utils.project import get_project_settings
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Engine = create_engine(URL(**get_project_settings()['DATABASE']))

__SessionMaker = sessionmaker(bind=Engine)
session = __SessionMaker()


def create_tables():
    Base.metadata.create_all(Engine)


class Entry(Base):

    __tablename__ = 'seyler'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column('id', Integer, primary_key=True)
    nick = Column('nick', String(255))
    entry_id = Column('entry_id', Integer)
    title = Column('title', String(255))
    entry_text = Column('entry_text', Text)
    date = Column('date', DateTime)
    category = Column('category', String(255))
    read_stat = Column('read_stat', String(255))
    share_stat = Column('share_stat', String(255))

    def __repr__(self):
        return '<Entry %s: %s>' % (self.title, self.entry_id)


if __name__ == '__main__':
    create_tables()

    session.close()