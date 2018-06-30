import os, sys
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TT2, APIC, TPE1, TALB, error

def add_img_cover_to_mp3(mp3_path, img_path):
    """
    The function adds cover images to mp3 files in the directories specified by path variables. 
    Use the same names for an mp3 file and the corresponding jpg/png file. 
    Existing audio tags will be cleared.
    """
    for item in os.listdir(mp3_path):
        if item[-4:] == '.mp3':
            audio = MP3(os.path.join(mp3_path, item), ID3=ID3)
            img_name = os.path.join(img_path, item[:-4])
            if os.path.isfile(img_name + '.jpg'):
                img = img_name + '.jpg' 
                mime = 'image/jpeg'
            elif os.path.isfile(img_name + '.png'):
                img = img_name + '.png' 
                mime = 'image/png'
            else:
                raise Exception('No image for the file ' + item)
            
            # clear audio tags if any
            try:
                audio.delete()
                audio.add_tags()
            except error:
                pass
            
            #add title
            audio.tags.add(TT2(encoding=3, text=item[:-4]))

            # add the cover image
            audio.tags.add(
                APIC(
                    encoding = 3, # utf-8
                    mime = mime, # image/jpeg or image/png
                    type = 3, # front cover image
                    desc = u'Cover',
                    data = open(img, 'rb').read()))
            
            # enter the artist in quotes on the next line if necessary
            audio.tags.add(TPE1(encoding=3, text=u""))
            
            # set album name to file name
            # each file should be in a separate album to have its own cover    
            audio.tags.add(TALB(encoding=3, text=item[:-4]))
            
            audio.save()

# set path to the mp3 files
try:
    mp3_path = sys.argv[1]
except:
    try:
        mp3_path = input('Enter the path to the mp3 files:')
    except:
        print('No mp3 path provided')

#set path to the images
try:
    img_path = sys.argv[2]
except:
    try:
        img_path = input('Enter the path to the images:')
    except:
        print('No img path provided')

try:
    add_img_cover_to_mp3(mp3_path, img_path)
except Exception as error:
    print(error)
