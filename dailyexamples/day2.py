'''
Day 2 : Printing & Comments
THis is a long comment 
and it extends
to multiple lines 
'''
print ('')
print('-' * 80) # String repetition

# BOLD, Center Alignment(:^), Color-Light Yellow(\033[93m)
print('\033[93m'+ '\033[1m' + '[{:^80}]'.format('Sweet Home Season 2:Netflix Renewal Status & Release Date'))
print('\033[0m' + '-' * 80)

# Print Multiple Lines
print('''
Sweet Home, 
Netflix’s latest \033[91mK-Drama horror\033[0m series has gotten off to a great start. 
After an impressive first season, 
plenty of subscribers are already looking ahead in hopes of a second season. 
''')
# String Format Method - Placeholder values 
print(' "{0}" is a Netflix {1} horror {2} series,'.format('Sweet Home','Original','K-Drama')) 
print ('based on the webtoon comic by \033[94m"{name}"\033[0m.'.format(name='Yongchan Hwang'))

# Spacing and without Spacing
print('The series is', 'produced by Studio Dragon,', 'who has also been responsible')
print('for' + 'other' + 'popular', '\033[4mK-Dramas\033[0m')
# Fill zero value at the beginning
print(' My Holo Love,'.zfill(25))
# End Parameter - No New Line
print("\'Love Alarm\', \'Arthdal Chronicles\',", end='~~~')
# Imoji repetition
print('Crash Landing on You.' + '🐍' * 5)

# Print "\"(escape)
print(r'New Line by \n')

print('\033[35m\033[46m' + ' need to capitalize '.upper() + '\033[0m') # Convert into Upper case
print(' need to capitalize '.capitalize()) # Convert the First Character to Upper case

# A Big Single line
print('\033[32m★' * 5 + '\033[0m More than you could ever know \
     Make my wish come true Baby, all \
          I want for Christmas... is you You, baby')