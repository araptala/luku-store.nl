import http.client
import json


conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

headers = {
    'content-type': "application/octet-stream",
    'X-RapidAPI-Key': "485377d487msh108c692813b6e2ap1203a3jsn23084661da34",
    'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
}

# Album List
conn.request("GET", "/search/?q=gucci%20mane&type=albums&offset=0&limit=10&numberOfTopResults=5", headers=headers)

# Album Tracks
# conn.request("GET", "/album_tracks/?id=3IBcauSj5M2A6lTeffJzdv&offset=0&limit=300", headers=headers)

res = conn.getresponse()
data = res.read()

data.decode("utf-8")

def spotify(request):
    try: 
        json_data = json.loads(data)
        artist = json_data['query']
        album_count = json_data['albums']['totalCount']
        album_name = json_data['albums']['items'][0]['data']['name']
        kwargs = json_data['albums']['items'][0]['data']['artists']['items'][0]['profile']['name']
    
        context = {
            'artist': artist,
            'album_count': album_count,
            'album_name': album_name,
            'kwargs': kwargs,
            }   
        return context
    except:
        print('Error trying to fetch the spotify api')
        pass



def mixcloud(request):

    # Set up the connection to the Mixcloud API
    conn = http.client.HTTPSConnection("api.mixcloud.com")

    # Make the request to get information about the user "djg400"
    conn.request("GET", "/djg400/?metadata=1")

    # Get the response from the server
    res = conn.getresponse()

    # Read the response body as JSON
    data = json.loads(res.read().decode())

    # Print the response data
    # print(f'This is the data: ', data)
    print_user_data(data)

def print_user_data(data):
    # print("Name:", data["name"])
    print("Username:", data["username"])
    # print("Bio:", data["biog"])
    print("Location:", data["city"], ",", data["country"])
    print("Follower count:", data["follower_count"])
    # print("Following count:", data["following_count"])
    # print("Cloudcast count:", data["cloudcast_count"])
    # print("Favorite count:", data["favorite_count"])
    # print("Listen count:", data["listen_count"])
    
    followers = data["follower_count"]
    username = data["username"]
    country = data["country"]
    follower_count = data["follower_count"]
    
    context = {
        'followers': followers,
        'username': username,
        'country': country,
        'follower_count': follower_count,
    }
    return context


def spotify_playlist():
    conn = http.client.HTTPSConnection("spotify23.p.rapidapi.com")

    headers = {
        'content-type': "application/octet-stream",
        'X-RapidAPI-Key': "485377d487msh108c692813b6e2ap1203a3jsn23084661da34",
        'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
    }

    conn.request("GET", "/playlist/?id=37i9dQZF1DX4Wsb4d7NKfP", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")