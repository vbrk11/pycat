import os

def find_file(name, path='C:/'):
    for root, dirs, files in os.walk(path):
        if name in files:
            result = os.path.join(root, name)
            return result

def cat(result):
    fin = open(result, 'r')
    file_contents = fin.read()
    print(file_contents)


def main():
   while True:
       prompt = str(input("[+] Enter your file name (or type exit to quit): "))
       if prompt.lower() == "exit":
           break
       
       result = find_file(prompt)
       
       if result:
           print()
           cat(result)
           print()
           
       else:
           print("[+] Couldn't find or read file")
           
main()
           
    
       
    
