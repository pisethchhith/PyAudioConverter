# Project name: Audio Converter
# Libraries I use: pydub, and os for opening file in os, Figlet
# Function:
    # interface
    # audioconvert
    # verifyaudiofile
    # title

from pyfiglet import Figlet
from pydub import AudioSegment, playback
import audioop # add audioop for enable audioConverter function to process
import os
import sys

def main():
    title("Audio Converter")
    print("""
1. Convert
2. Playback
3. Exit
""")
    while True:
        try:
            user = input("Choose your approach: ")
            if user == "1":
                file = input("Enter audio file: ")
                format = input("Enter audio format would you like to convert?: ")
                verifyAudioConverter(file, format)
                audioConverter(file, format)
                break
            # add playback interface to play audio file 
            elif user == "2":
                try:
                    file = input("Enter audio file to play: ")
                    audio = AudioSegment.from_file(file)
                    playback.play(audio)
                    break
                except(KeyboardInterrupt, EOFError):
                    main()
            # exit the program
            elif user == "3":
                sys.exit("Thank You for using my product")
            else:
                raise NameError
        
        except NameError:
            print("Please choose valid options")
            continue

def verifyAudioConverter(file, format):
    # verify if audio file are required [MP3, WAV, OGG, FLAC (for lossless), M4A, AAC]
    try:
        formats = ["mp3", "wav", "ogg", "flac", "aac", "m4a"]
        if file.split(".")[-1] in formats:
            pass
        else:
            raise ValueError
    except ValueError:
        sys.exit("Please choose valid file")

    print(f"""
You are converting from {file} to {format}
Are you sure?

1.Yes
2.No
""")
    while True:
        user = input("Choose approach: ")
        if user == "1":
            break
        elif user == "2":
            main()
            break
        else:
            pass


def audioConverter(file, formats):
    # get absolute file from os
    filepath = os.path.abspath(file)
    filebase = os.path.basename(file)
    fileext = file.split(".")[-1]

    print(f"Proceed conversion from {fileext} to {formats}")
    # execute only on different type of audio

    if not (filebase.endswith(str("." + formats))):

        audio = AudioSegment.from_file(file, fileext)
        newname = filebase.replace(fileext, formats)
        # save exported file with same as original file name
        newpath = filepath.replace(file, newname)
        audio.export(newpath, format=formats)
        print(f"Audio file saved to {newpath}")

# Decorate title on welcoming interface
def title(text):
    figlet = Figlet()
    figlet.setFont(font="big")
    print(f"{figlet.renderText(text)}")

if __name__ == "__main__":
    main()
