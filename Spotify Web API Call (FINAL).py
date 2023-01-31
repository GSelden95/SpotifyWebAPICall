#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#You have to install some things on your terminal to begin with... follow along: 
#In terminal: pip install spotipy

#In terminal: pip install "requests[security]"

#In terminal: sudo pip install --upgrade pip


# In[ ]:


#Importing SpotiPY and Client Credentials
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# In[ ]:


#Make an account with Spotify and obtain your API and Client Credientials. Set up API Key, Client Secret and SpotiPY Client Credential Call

api_key = 'put api key here'
client_secret = 'put client secret here'
client_credentials = SpotifyClientCredentials(client_id=api_key, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials)


# In[ ]:


#Import requests. You'll need it to GET Api information
import requests


# In[ ]:


#General API calls:
spotify_api_link = 'https://api.spotify.com'
spotify_api_request = requests.get(spotify_api_link)

spotify_request = requests.get(f'put api link here',headers={'Authorization':'put api key here',
                               'Host' : 'api.spotify.com','Content-Type': 'application/json'})


# In[ ]:


#Check to see the status code. This will tell us if we called the API correctly
spotify_api_request.status_code


# In[ ]:


#importing pandas. A cleaning tool for tables and matrices on python
import pandas as pd


# In[ ]:


main_table_one = pd.DataFrame(columns = ['href', 'items', 'limit', 'next', 'offset', 'previous', 'total', 'track names', 'artist', 'popularity', 'album', 'duration (ms)', 'genre', 'available markets', 'id', 'uris', 'total playlist followers', 'total artist followers'])


# In[ ]:


main_table_one


# In[ ]:


audio_final_table_table = pd.DataFrame(columns = ['href', 'items', 'limit', 'next', 'offset', 'previous', 'total', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track href', 'analysis url', 'duration (ms)', 'time signature'])


# In[ ]:


audio_final_table_table


# In[ ]:


#Let's parse through and see what genres we can input in the following command!!! Wow, a lot of genres!!!
#Step one!!!!
#Only run this one time!!!!!!
recomended_genres = sp.recommendation_genre_seeds()


# In[ ]:


#Only run this one time!!!!
recomended_genres['genres']


# In[ ]:


#Step 2. DON'T RUN ANYTHING ELSE ABOVE. YOU ONLY NEEDED TO DO THAT ONE TIME ONLY!!!!
#Run everything from here on out every time!!! Repeat this workflow!!!
while True:
    genre = input('What genre would you like? \n')
    if genre in recomended_genres['genres']:
        print("Nice choice!!!")
        break
    else:
        print("This is not a genre \n")
    


# In[ ]:


genre_search = sp.search(genre, limit=50, type='playlist')


# In[ ]:


playlist_search = genre_search['playlists']['items'][0]['uri'] 


# In[ ]:


#Obtaining starter album information such as track name, album name, uri, track number in album, etc from playlist_items command. 
playlist_items = sp.playlist_items(playlist_search , limit=100, offset=0)


# In[ ]:


#The command I call calls 50 positional playlists. The number you choose here is which playlist out of 50 (0-49) you want. 
#If you choose a number less than 0 or greater than 49, it will spit out an error message. 
#If you've chose a particular genre and you only want one genre, THEN DON'T RUN THE CODE PRIOR TO THIS!!! 
#JUST START FROM HERE!!!
index = int(input())


# In[ ]:


def put_in_index(index):

    playlist_call = genre_search['playlists']['items'][index]['uri'] 

    playlist_table = sp.playlist_items(playlist_call, limit=100, offset=0)  
    
    playlist_table_followers = sp.playlist(playlist_call)

    playlist_table['track names'] = []
    playlist_table['artist'] = []  
    playlist_table['popularity'] = []
    playlist_table['album'] = []
    playlist_table['duration (ms)'] = []
    playlist_table['genre'] = []
    playlist_table['available markets'] = []
    playlist_table['id'] = []
    playlist_table['uris'] = [] 
    playlist_table['total playlist followers'] = []
    playlist_table['total artist followers'] = []
    
    for i in range(len(playlist_table['items'])):
        artist_table_followers = sp.artist(playlist_table['items'][i]['track']['artists'][0]['uri'])
        playlist_table['total artist followers'].append(artist_table_followers['followers']['total'])
      

    for i in range(len(playlist_table['items'])):
        playlist_table['track names'].append(playlist_table['items'][i]['track']['name'])
        playlist_table['artist'].append(playlist_table['items'][i]['track']['artists'][0]['name'])
        playlist_table['popularity'].append(playlist_table['items'][i]['track']['popularity'])
        playlist_table['album'].append(playlist_table['items'][i]['track']['album']['name'])
        playlist_table['duration (ms)'].append(playlist_table['items'][i]['track']['duration_ms'])
        playlist_table['genre'].append(genre)
        playlist_table['available markets'].append(playlist_table['items'][i]['track']['available_markets'])
        playlist_table['id'].append(playlist_table['items'][i]['track']['id'])
        playlist_table['uris'].append(playlist_table['items'][i]['track']['uri'])
        playlist_table['total playlist followers'].append(playlist_table_followers['followers']['total'])
        
    return playlist_table


# In[ ]:


#It shouldn't but if this code crashes run it again. 
table = put_in_index(index)


# In[ ]:


table_one = pd.DataFrame(table)


# In[ ]:


table_one


# In[ ]:


#So now let's add our audio qualities!!! Make sure the index in the following function is the same index as put_in_index.
def audio_table(index):

    playlist_call_building = genre_search['playlists']['items'][index]['uri'] 
    
    playlist_table_two = sp.playlist_items(playlist_call_building, limit=100, offset=0)  
    
    for i in range(len(table['uris'])):
        audio_qualities = sp.audio_features(table['uris'])
        audio_qualities.append(audio_qualities)

    return audio_qualities


# In[ ]:


#It shouldn't but if this code crashes run it again. 
audio_table_table = audio_table(index)


# In[ ]:


def audio_table_dataframe(index):

    playlist_call_building = genre_search['playlists']['items'][index]['uri'] 
    
    playlist_table_two = sp.playlist_items(playlist_call_building, limit=100, offset=0) 

    playlist_table_two['danceability'] = []
    playlist_table_two['energy'] = []
    playlist_table_two['key'] = []
    playlist_table_two['loudness'] = []
    playlist_table_two['mode'] = []
    playlist_table_two['speechiness'] = []
    playlist_table_two['acousticness'] = []
    playlist_table_two['instrumentalness'] = []
    playlist_table_two['liveness'] = []
    playlist_table_two['valence'] = []
    playlist_table_two['tempo'] = []
    playlist_table_two['type'] = []
    playlist_table_two['id'] = []
    playlist_table_two['uri'] = []
    playlist_table_two['track href'] = []
    playlist_table_two['analysis url'] = []
    playlist_table_two['duration (ms)'] = []
    playlist_table_two['time signature'] = []

    for i in range(len(playlist_table_two['items'])):
        playlist_table_two['danceability'].append(audio_table_table[i]['danceability'])
        playlist_table_two['energy'].append(audio_table_table[i]['energy'])
        playlist_table_two['key'].append(audio_table_table[i]['key']) 
        playlist_table_two['loudness'].append(audio_table_table[i]['loudness'])
        playlist_table_two['mode'].append(audio_table_table[i]['mode'])
        playlist_table_two['speechiness'].append(audio_table_table[i]['speechiness'])
        playlist_table_two['acousticness'].append(audio_table_table[i]['acousticness']) 
        playlist_table_two['instrumentalness'].append(audio_table_table[i]['instrumentalness'])
        playlist_table_two['liveness'].append(audio_table_table[i]['liveness'])
        playlist_table_two['valence'].append(audio_table_table[i]['valence'])
        playlist_table_two['tempo'].append(audio_table_table[i]['tempo'])
        playlist_table_two['type'].append(audio_table_table[i]['type']) 
        playlist_table_two['id'].append(audio_table_table[i]['id'])
        playlist_table_two['uri'].append(audio_table_table[i]['uri'])
        playlist_table_two['track href'].append(audio_table_table[i]['track_href'])
        playlist_table_two['analysis url'].append(audio_table_table[i]['analysis_url'])
        playlist_table_two['duration (ms)'].append(audio_table_table[i]['duration_ms'])
        playlist_table_two['time signature'].append(audio_table_table[i]['time_signature'])
        
    return playlist_table_two


# In[ ]:


len(audio_table_table)


# In[ ]:


#For some reason the entire list repeats itself in the last element, adding an additional element, use this code to erase it. No additional work!!!
for n in range(len(audio_table_table)):
    last_var = audio_table_table[n]
audio_table_table.remove(audio_table_table[n])


# In[ ]:


len(audio_table_table)


# In[ ]:


audio_dataframe = audio_table_dataframe(index)


# In[ ]:


audio_final_table = pd.DataFrame(audio_dataframe)


# In[ ]:


audio_final_table


# In[ ]:


audio_final_table.columns


# In[ ]:


audio_final_table_table = pd.concat([audio_final_table_table, audio_final_table], ignore_index = True)


# In[ ]:


main_table_one = pd.concat([main_table_one, table_one], ignore_index = True)


# In[ ]:


main_table_one


# In[ ]:


audio_final_table_table


# In[ ]:


#DON'T RUN THIS CODE UNTIL YOU HAVE ALL THE ROWS YOU WANT!!!
so_close = pd.merge(audio_final_table_table, main_table_one, how = 'outer', on = 'id')


# In[ ]:


so_close


# In[ ]:


so_close.columns


# In[ ]:


final_table = so_close.drop(columns = ["href_y", "items_y", "limit_y", "next_y", "offset_y", "previous_y", "total_y"])


# In[ ]:


final_table


# In[ ]:


final_table.columns


# In[ ]:


#DO NOT RUN THIS UNTIL YOU ARE SURE YOU HAVE EVERYTHING YOU NEED IN YOUR CSV!!!
final_table.to_csv('.csv')

