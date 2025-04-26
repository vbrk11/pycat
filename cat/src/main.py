"""
   Copyright (C) 2025 
   
   https://github.com/vbrk11

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License along
   with this program; if not, write to the Free Software Foundation, Inc.,
   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
   
"""

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
           
    
       
    
