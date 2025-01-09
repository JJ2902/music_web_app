from lib.album_repository import *
from lib.album import *
"""
when I call #all
I get all the albums in the albums table
"""

def test_all(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1,'Doolittle', 1989, 1)
    ]

"""
when I call #create
I create an album in the albums table
And I can see it back in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None,'test title', 1000, 2)
    repository.create(album)
    assert repository.all() == [
        Album(1,'Doolittle', 1989, 1),
        Album(2,'test title', 1000, 2)
    ]
    
