#from genericpath import isdir
import os, shutil
from pathlib import Path
import asyncio, aioshutil
from aiopath import AsyncPath
import os
#from sys import argv, platform
#import re

GENERENION = ''

types = ['images', 'documents', 'videos', 'audios', 'archives','other']
image_type = ['.jpg', '.png', '.jpeg','.svg']
video_type = ['.avi', '.mp4', '.mov','.mkv']
doc_type = ['.doc','.pdf', '.docx', '.txt', '.xlsx','.pptx']
music_type = ['.mp3', '.ogg', '.wav', '.amr']
archives = ['.zip', '.7zip', '.gz', '.tar']


def normalize(string):

    alphabet = {ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'G', ord('Д'): 'D', ord('Е'): 'E',
            ord('Ё'): 'E', ord('Ж'): 'ZH',ord('З'): 'Z', ord('И'): 'I', ord('К'): 'K', ord('Л'): 'L',
            ord('М'): 'M', ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P', ord('Р'): 'R', ord('С'): 'S',
            ord('Т'): 'T', ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'H', ord('Ц'): 'TS', ord('Ч'): 'CH',
            ord('Ш'): 'SH', ord('Щ'): 'SCH', ord('Ъ'): '`', ord('Ы'): 'I',ord('Ь'): '`', ord('Э'): 'E',
            ord('Ю'): 'JU', ord('Я'): 'JA', ord('а'): 'f', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g',
            ord('д'): 'd', ord('е'): 'e', ord('ё'): 'e', ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'i',
            ord('к'): 'k', ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p',
            ord('р'): 'r', ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f', ord('х'): 'h',
            ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'sch', ord('ъ'): '`', ord('ы'): 'i',
            ord('ь'): '`', ord('э'): 'e', ord('ю'): 'ju', ord('я'): 'ja'}
    
    list_New = []

    normalized = ''

    for c in string:
        if not c.isalpha() and not c.isdigit():
            c = '_'
            list_New.append(c)
        else:
            c = c.translate(alphabet)
            list_New.append(c)
    return normalized.join(list_New)


def create_folders():
    for name in types:
        directory = os.path.join(GENERENION, name)
        try:
            os.stat(directory)
        except:
            os.mkdir(directory)

async def relocateFile(filesInfo):

    create_folders()
    queue = asyncio.Queue()
    task_list = []
    info = filesInfo.split(";")

    src = os.path.join(info[1], info[2]+info[3])

    dest = os.path.join(GENERENION, info[0], normalize(info[2])+info[3])
    
    if info[0] == 'archives':
        await aioshutil.unpack_archive(await aioshutil.move(src, dest),os.path.join(GENERENION, info[0]))
        os.remove(dest)
        
    else:
        task = asyncio.create_task(aioshutil.move(src, dest))
        task_list.append(task)


    await queue.join()
    await asyncio.gather(*task_list, return_exceptions=True)      
    
async def fileDistribute(fileCollections, path, nestingDeep):

    for file in fileCollections:
        fileName, fileExtension = os.path.splitext(file)
        if fileExtension in image_type:
            await relocateFile(f'images;{path};{fileName};{fileExtension}')
        elif fileExtension in video_type:
            await relocateFile(f'videos;{path};{fileName};{fileExtension}')
        elif fileExtension in doc_type:
            await relocateFile(f'documents;{path};{fileName};{fileExtension}')
        elif fileExtension in music_type:
            await relocateFile(f'audios;{path};{fileName};{fileExtension}')
        elif fileExtension in archives:
            await relocateFile(f'archives;{path};{fileName};{fileExtension}')
        else:
            await relocateFile(f'other;{path};{fileName};{fileExtension}')
        
async def walk(path, nestingDeep=0):
    fileCollections = []
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
           await walk(os.path.join(path, file), nestingDeep + 1)
        else:
            fileCollections.append(file)
    await fileDistribute(fileCollections, path, nestingDeep)

def del_empty_dirs(path):
    for el in os.listdir(path):
        fold = os.path.join(path, el)
        if os.path.isdir(fold):
            del_empty_dirs(fold)
            if not os.listdir(fold):
                os.rmdir(fold)

async def main():

    global GENERENION
    print('I need the folder path to sort. \nFor example: C:\\blabla\\bla...')

    while True:
        user_input = input()
        main_path = Path(user_input)

        if user_input.casefold() == 'cancel':
            print('Canceling sorting...')
            is_sorted = False
            return is_sorted

        elif main_path.exists() and os.path.isdir(main_path):

            print(f'The folder which I will sort is: {main_path}\n')
            print('Sorting, please wait...')
            GENERENION = main_path
            await walk(main_path)
            del_empty_dirs(main_path)
            is_sorted = True
            print('Your folder has been sorted!')
            return is_sorted
            
        else:
            print('This folder doesn\'t exist. \nPlease try again or write "cancel" to cancel sorting.')


    
if __name__ == '__main__':
    asyncio.run(main())