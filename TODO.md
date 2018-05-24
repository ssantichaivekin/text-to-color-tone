Todo:

We want to find the correlation between characters/phonemes and their respective color tone. In order to do this we will need to use a dictionary to seperate words into different groups (accorsing to their characters or phonemes) and run the KNN on different groups and compare them against each other. How will we achieve that?

Part 1:
We should get this inside the dict folder
We use NLTK library dictionary to seperate the dictionary into word groups. We want to implement these functions:
1. get_num_syllable # get the number of syllables of the word
2. get_type # return 'noun', 'verb', 'adjective', 'adverb', ...
2. is_concrete_noun # ask whether a noun is abstract or concrete
3. starts_with_vowel # check whether if a word starts with vowel or a consonant
4. get_consonant_sound(syllable_index) # get the sleading consonant sound of that index
5. get_vowel_sound(syllable_index) # get the vowel sound of that index

We will write these functions in the dict folder.

We then seperate words to different groups. Here are some groups I am interested:
: Meaning and Functions (5 groups total)
1. all words 
2. all concrete nouns (wood, phone, battery)
3. all abstract nouns (love, hate, cry)
4. all verbs
5. all adjectives
: Characters and Phonemes (like 100+ groups I guess)
1. all words
2. words that begins with a consonant
3. words that begins with a vowel
2. words that begins with character a/b/c/d
3. words that begins with the sound ...
4. words that has the fist vowel sound ...

Of course, we are also creating a mix between these two groups.

Part 2:
Download the image information. The best way to keep these pictures is to just remember the dominant featuers for these numbers. We should separate our search into chunks, so that we don't have to rerun the search in case we screw up. I am thinking that one chuck should have ~100 words. Each chuck should store one text file outlining the pixel_id and its corresponding occurance (just think of buckets).
1. Get Google search API
2. Write the python function to search and download the thumbnails (~20 pics per word)
3. These thumbnails are surprisingly small in size, so we can keep all of them in the cloud. It will take some time to download all of them though.
4. Run KNN on each of these and keep only some of its representative color (say 10). Then store each of them in a file.
4. We run those functions in the could through a remote server.

Part 3:
Running Scikit's KNN and visualization. This will be the easy part.
1. Use the info from part 1 and 2 to process the KNN for each group.


Done:

Part 0 :
1. Use Google search API to search images using the text as the query.
2. Obtain from the search thumbnails (6 by default) of the text.
3. Use KNN (K nearest neighbors) algorithm on the thumnails to get colors (3 by default) that best represent the pixel concatenation.
4. Display the colors (called collectively as color tone) using matplotlib.
5. Add pictures to README.md
6. Allow the application to be run from command line
7. Finalize README.md
8. Allow people to change num_clusters from command line.