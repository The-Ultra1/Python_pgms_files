from pathlib import Path,sys,os
import colorama
from colorama import Fore,Style
colorama.init(autoreset=True)

fileFormats = {file.suffix[1:] for file in Path().glob('**/*')}
fileFormats.discard('')

Prompt_msg='''Enter your file format (if more than one format use comma)
Just type "all" if you want for all file formats '''

print(Fore.LIGHTYELLOW_EX + Prompt_msg)

inp_file_Formats=set(input("Your file format(s) : ").lower().split(","))
fileFormats = fileFormats if 'all' in inp_file_Formats else fileFormats.intersection(inp_file_Formats)

while fileFormats:
    FolderName=fileFormats.pop() + "_files"
    Path(FolderName).mkdir(exist_ok=True)
    target_Dir = str(Path().absolute()) + "\\" + FolderName
    for file in Path().glob('*.'+FolderName[:-6]):
        try:
            if(file.name==Path(__file__).name):
                continue
            Moved_Location = file.rename(target_Dir+"\\"+file.name)
            print(Fore.LIGHTCYAN_EX + "Filed Moved | " + file.name)
        except FileExistsError:
            print(Fore.LIGHTRED_EX + "File Already exists | "+file.name)
        except PermissionError:
            print(Fore.LIGHTRED_EX + "File being used by another process | "+file.name)
        except:
            print(Fore.RED + str(sys.exc_info()[1])+" | "+file.name)
    if not(os.listdir(FolderName)):
        os.rmdir(FolderName)

print(Fore.LIGHTCYAN_EX + "*"*20 + " Process Completed " + "*"*20 +"\nAny key to close....!")
input()
