from functions import *

print("1. Audio\n2. Visual\n3. Other\n4. Add item TEST")

choice = int(input("Enter your choice: "))

if choice == 4:
    addAudioItem()

if choice == 1 or 2 or 3:
    viewSelect()

if choice == 1:
    viewAudio()