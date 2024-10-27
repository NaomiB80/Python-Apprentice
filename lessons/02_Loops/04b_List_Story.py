"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽', 'they']

story = []

story = story + words[:1] + words[2:3] + words[7:8] + words[9:10] + [','] + words[7:8]
story = story + words[-7:-6] + words[-5:-4] + words[6:7] + ['her'] + words[-8:-7] 
story = story + words[10:11] + words[8:9] + words[4:5] + words[10:11] + words[-3:-2] 
story = story + words[6:7] + words[7:8] + words[-2:-1] + words[-6:-5] + words[5:6]
story = story + words[7:8] + words [1:2] + words[6:7] + words[7:8] + words[3:4] + [',']
story = story + words[-6:-5] + words[-1:] + ['played'] + ['together'] + ['.']
# Create a story using the words in the list

# Display the story to the user
print(' '.join(story))