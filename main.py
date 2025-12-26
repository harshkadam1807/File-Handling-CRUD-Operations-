from pathlib import Path
import os     #for deleting function using remove

def filesandfolderslist():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f'{i+1} : {items}')

def createfile():
    try:
        filesandfolderslist()
        name = input('Enter file name which you want to create: ')
        p=Path(name)
        if not p.exists():
            with open (p,'w') as f:
                data=input('Enter data you want to write: ')
                f.write(data)
            print('File Successfully Created')
        else:
            print('File Already Exits')
    except Exception as error:
        print(F'Error occured as {error}')

def readfile():
    try:
        filesandfolderslist()
        name=input('Enter file name which you want to read: ')
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as f:
                data=f.read()
                print(data)
            print('File Readed Succesfully')
        else:
            print('File does not Exits')
    except Exception as error:
        print(f'An error occured as {error}')

def updatefile():
        try:
            filesandfolderslist()
            name=input('Enter file name which you want to update: ')
            p = Path(name)
            if p.exists() and p.is_file():
                print('press 1 for changing file name of your file: ')
                print('press 2 for writing data in your file: ')
                print('press 3 for appending data in your file')

                updatingchoice=int(input('Enter your Updating choice: '))

                if updatingchoice == 1:
                    New_file_name=input('Enter your new file name: ')
                    p2=Path(New_file_name)
                    p.rename(p2)
                if updatingchoice == 2:
                    with open(p,'w') as f:
                        data=input('Enter data you want to write this will overwrite your previous data: ')
                        f.write(data)
                if updatingchoice == 3:
                    with open(p,'a') as f:
                        data=input('Enter data you want to write: ')
                        f.write(data)

        except Exception as error:
            print('An error occured as {error}')

def deletefile():
    try:
        filesandfolderslist()
        name=input('Enter file nam which you want to delete: ')
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print('File removed succesfully')
        else:
            print('File doesnt exists')
    except Exception as error:
        print(f'An error occured as {error}')

print('Press 1 to create a file: ')
print('Press 2 to read a file: ')
print('Press 3 to udpate a file: ')
print('Press 4 to delete a file: ')

choose=int(input('Enter your choice: '))

if choose == 1:
    createfile()

if choose == 2:
    readfile()

if choose == 3:
    updatefile()

if choose == 4:
    deletefile()