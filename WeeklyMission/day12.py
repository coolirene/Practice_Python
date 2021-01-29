# Day 12. Tuples, Dictionaries and Sets
# Tuple - 5 String Values
print()
marvel_tuple = ('Guardians of the Galaxy', 'Spider-Man: Far From Home', 'X-Men',
               'Avengers: Infinite War', 'Doctor Strange: In The Multiverse of Madness')
# For Dictionary Key - enumerate
m_dict = dict(enumerate(marvel_tuple))   
# Adding Strings to keys and get the length of Values
len_dict = {f'{key}번째 문자열 길이': len(value) for key, value in m_dict.items()}
print(len_dict)
print()
