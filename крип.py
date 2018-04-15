cryptMode = input("[E]ncrypt|[D]ecrypt: ").upper()
if cryptMode not in ['E','D']:
	print("Error: mode is not Found!"); raise SystemExit
startMessage = input("Write the message: ").upper()
try:rotKey = int(input("Write the key: "))
except ValueError: print("Only numbers!"); raise SystemExit
def encryptDecrypt(mode, message, key, final = ""):
	for symbol in message:
		if mode == 'E':
			final += chr((ord(symbol) + key - 13)%26 + ord('A'))
		else:
			final += chr((ord(symbol) - key - 13)%26 + ord('A'))
	return final
print("Final message:",encryptDecrypt(cryptMode, startMessage, rotKey))
try:
    namefile=input("File name: ")
    with open (namefile, 'ab') as file:
        text=(encryptDecrypt(cryptMode, startMessage, rotKey))
        file.write(text.encode("utf-8"))
except FileNotFoundError:
    print("[x] File: '"+str(namefile)+"' is not defined!")
    raise SystemExit
else:
    print("[+] File: "+str(namefile)+" successfully overwritten!")