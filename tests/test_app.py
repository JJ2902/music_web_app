# Tests for your routes go here

# === Example Code Below ===

# """
# GET /emoji
# """
# def test_get_emoji(web_client):
#     response = web_client.get("/emoji")
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

# Post /albums
#  title: 'DooMore'
#   release_year: 1999
#   artist_id: 1
#Expected Response (200 OK)

# GET /albums
# Expected Response (200 OK)

# ```
# Album(1,'Doolittle', 1989, 1)
# Album(2,'DooMore', 1999, 1)
# ```

"""
When I call POST /albums with album info
That album is now in the list in GET/albums

"""

def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("albums", data={
        'title': 'DooMore',
        'release_year': '1999',
        'artist_id': '1'
    })

    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/albums")
    assert post_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, DooMore, 1999, 1)"
    
"""
When I call GET /albums
I get a list of albums back

"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Album(1, Doolittle, 1989, 1)"


# # Post /albums
# #Expected Response (400 Bad Request)

def test_post_albums_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums")

    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "" \
        "You need to submit a title, release_year, and artist_id"
    
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Doolittle, 1989, 1)"


# # Request:
# GET /artists

# # Expected response (200 OK)
# Pixies, ABBA, Taylor Swift, Nina Simone

"""
When I call GET /artists
I get a list of artists back

"""
def test_get_artist(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Artist(1, Pixies, Rock)\n" \
        "Artist(2, ABBA, Pop)\n" \
        "Artist(3, Taylor Swift, Pop)\n" \
        "Artist(4, Nina Simone, Jazz)" 

# # Request:
# POST /artists

# # With body parameters:
# name=Wild nothing
# genre=Indie

# # Expected response (200 OK)
# (No content)

# # Then subsequent request:
# GET /artists

# # Expected response (200 OK)
# Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing

"""
When I call POST /artists with artist info
That artist is now in the list in GET/artists

"""

def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/artists", data={
        'name': 'Wild nothing',
        'genre': 'Indie'
    })
    
    invalid_post_response = web_client.post("/artists", data={})

    assert invalid_post_response.status_code == 400
    assert invalid_post_response.data.decode('utf-8') == "" \
        "You need to submit an artist name and genre."
    # assert post_response.status_code == 200
    # assert post_response.data.decode('utf-8') == "" \
        
    


    get_response = web_client.post("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Artist(1, Pixies, Rock)\n" \
        "Artist(2, ABBA, Pop)\n" \
        "Artist(3, Taylor Swift, Pop)\n" \
        "Artist(4, Nina Simone, Jazz)\n" \
        "Artist(5, Wild nothing, Indie)" 






