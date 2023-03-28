    #list comprehension
# lists = [2, 5, -1, -23, 10]
# res = [int(l) for l in lists if l<0]
# print(res)


    #from video create audio
# import moviepy.editor
# from pathlib import Path

# video_file = Path('my_videp.mp4')

# video = moviepy.editor.VideoFileClip(f'{video_file}')
# audio = video.audio
# audio.write_audiofile(f'{video_file.stem}.mp3')


    #encrypt and decrypt file
# import pyAesCrypt

# password = input('Enter password for file: ')
# #encrypt
# pyAesCrypt.encryptFile('file.txt', 'file.txt.aes', password)
# #decrypt
# pyAesCrypt.decryptFile('file.txt.aes', 'file.txt', password)


    # create password for file
# from PyPDF2 import PdfFileWriter, PdfFileReader
# from getpass import getpass

# pdfwrite = PdfFileWriter()
# pdf = PdfFileReader('File.pdf')

# for page in range(pdf.numPages):
#     pdfwrite.add_page(pdf.pages[page])
    
# password = getpass(prompt='Enter password: ')
# pdfwrite.encrypt(password)

# with open('protect.pdf', 'wb') as file:
#     pdfwrite.write(file)
    

    #find size 
# import sys
# first = [val+3 for val in range(1000)]
# print(first)
# print(sys.getsizeof(first))
# next = 5
# print(sys.getsizeof(next))


    #collection
# from collections import Counter
# x = Counter('abracadabra').most_common(3)
# print(x)


    #dict of dicts
# import json
# print(json.dumps({'a':2, 'b':{'x':3, 'y':{'t1': 4, 't2':5}}}, sort_keys=True, indent=4))


    #all data now
# import datetime
# now = datetime.datetime.now()
# y, mth, d, h, m, s = now.year, now.month, now.day, now.hour, now.minute, now.second
# text = 'Visited: {} yer, {} month, {} day, {} hour, {} min, {} sec'
# print(text.format(y, mth, d, h, m, s))


    #image for ASCII
# from pywhatkit import image_to_ascii_art as tk
# img = 'img.png'
# text = 'text'
# tk(img, text)


    #text for ASCII
# import pyfiglet 
# text = pyfiglet.figlet_format(text='coder', font='isometric1')
# print(text)
# text1 = pyfiglet.print_figlet(text='coder', colors='BLUE', )
# print(text1)


    #random text 
# import random
# import string
# letters = string.ascii_lowercase
# rand_string = ''.join(random.choice(letters) for _ in range(5))
# print(rand_string)


    #check type data True or False
# x = 10
# print(isinstance(x, int))
# print(isinstance([3, 2, 1], list))
# print(isinstance('hello', str))


    #text ---  throught unicode
# x = 'hello'
# y = ''
# for i in x:
#     y += i+'\u0336'
# print(y)


    #make bool variables: True and False
# import sys
# sys.allow_boolean_assignment = 1
# True = False
# if True:
#     print('Now True')
# else:
#     print('Now false')


    #get holidays
# import holidays
# for p in holidays.UKR(years=2023).items():
#     print(*p)


    #get joke with python
# import pyjokes
# print(f'< {pyjokes.get_joke()} >')


    #remove worst object 
# from itertools import compress
# lst = ['name', 'kombo', 'age', 'old', 'tom']
# lst_1 = [1, 0, 1, 1, 0]
# res = list(compress(lst, lst_1))
# print(res)


    #create QRcode photo
# import qrcode
# data = 'https://www.instagram.com/deennill/'
# file_name = 'qrcode.png'
# img = qrcode.make(data)
# img.save(file_name)


    #make screenshot
# import pyscreenshot
# img = pyscreenshot.grab(bbox=(10, 10, 4000, 2000))
# img.show()
# img.save('screen.png')


    #get position element(e) in text  and ende element 
# text = 'python learening'
# a = text.rfind('e') #12
# b = text.endswith('g') # true or 0
# print(a+b)



