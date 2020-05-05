# Import of library
from zipfile import ZipFile

# Variable names
zip_file = 'test_zip.zip'
eng_dict = 'english.txt'
check = 0 

# Move the words from txt file to a list
with open(eng_dict) as ed:
    content = ed.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

# Brute Force until we find the right password
i = 1
print('Hacking', end='')
for password in content:
    if (i%5000==1):
        print('.', end='', flush=True)
    try:
        with ZipFile(zip_file) as zf:
            zf.extractall(pwd=bytes(password,'utf-8'))
        check = 1
    except Exception:
        check = 0
        pass
    if check ==1:
        break;
    i = i + 1

print('')
print('FILE UNLOCKED')
