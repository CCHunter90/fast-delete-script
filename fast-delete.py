#this is a script for emptying a folder quickly
import os
import time
print('''
This is a python script created for helping cleaning big folders in an easy way. 
Make sure you want to delete all the files before you start the process, 
cause will be deleted permanently. 
Knowing this, please follow the following steps:
''')
delete_folder_location = str(input('Introduce la dirección de la carpeta o directorio a vaciar: '))
print('''
WARNING!! USING THIS SCRIPT SEVERAL TIMES CAN DAMAGE CPU LIFETIME
AS IT REQUIRES A BIG PERCENTAGE OF IT WHILE EXECUTING. CHOOSE WETHER IF
YOU WOULD LIKE FASTEST DELETING INJURING YOUR CPU OR CHOOSE SLOWER DELETING:''')
def speedChooser():
    print('please choose a valid speed option')
    speed = input('f (fastest)/s (slower)')
    speed = str(speed)
    if speed == 'f' or speed == 's':
        return speed
    else:
        speed = speedChooser()

speed = input('f (fastest)/s (slower): ')
speed = str(speed)

if speed == 'f' or speed == 's':
    pass
else:
    speed = speedChooser()

def modeChooser():
    print('choose a valid mode option (repeat/once)')
    mode = input('Choose mode (repeat/once): ')
    if mode == 'repeat' or mode == 'once':
        return mode
    else:
        mode = modeChooser()



mode = input('Choose if you want to keep script working forever to delete incoming files to this folder or if you want it to work just once: (repeat/once): ')
mode = str(mode)

if mode == 'repeat' or mode == 'once':
    pass
else:
    mode = modeChooser()

if speed == 's':
    print('Slow mode is enabled, you can return later to check how is it going')
if mode == 'repeat':
    print('Repeat mode is enabled. Script will search for new files until stoped')
time.sleep(2)

def delete(delete_folder_location,sub_folder):
    while True:
        delete_folder_content = os.listdir(delete_folder_location)
        for each in delete_folder_content:
            try:
                os.remove(f'{delete_folder_location}/{each}')
                print(f'File {each} deleted')
            except Exception as e:
                e = str(e)
                if e == f"[Errno 21] Is a directory: '{delete_folder_location}/{each}'":
                    path = os.path.join(delete_folder_location,each)
                    try:
                        os.rmdir(path)
                    except:
                        print(f'opening folder {path}')
                        delete(path,True)
            if speed == 's':
                time.sleep(0.1)
        if os.listdir(delete_folder_location) == []:
            if sub_folder == True:
                return('Finished process, restart to delete an other folder. Tip: Put all the files and folders you want to delete all together for faster delete')
            else:
                if mode == 'repeat':
                    hour = time.strftime('%H:%M:%S')
                    print(f'{hour} - Repeat mode is enabled, checking for new files to delete...')
                    time.sleep(1)
                else:
                    return('Finished process, restart to delete an other folder. Tip: Put all the files and folders you want to delete all together for faster delete')

delete(delete_folder_location,False)