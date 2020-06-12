playlist = {
    'title': 'Coding',
    'author': 'Elemento24',
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duration':2.5},
        {'title': 'song2', 'artist': ['blue', 'djcat'], 'duration':5.5},
        {'title': 'mewmew', 'artist': ['garfield'], 'duration':2}
    ]
}

total_length = 0

for song in playlist['songs']:
    total_length += song['duration']

print(total_length)
