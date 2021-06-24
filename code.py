import pytube
import os
from pytube import YouTube


def main():
    video_url = input('Enter YouTube video URL : ')

    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'

 # Naming the audio track same as youTube id.
    name = pytube.extract.video_id(video_url)

    # Filtering out only the audio track
    YouTube(video_url).streams.filter(
        only_audio=True).first().download(filename=name)

    # Setting the saving location with right extension.
    location = path + name + '.mp4'
    renametomp3 = path + name + '.mp3'

    ''' The name of the operating system dependent module for me is 'nt' (in Windows) 
    You can Check yours by only running -->>import os
                                            print(os.name)  '''

    if os.name == 'nt':
        os.system('ren {0} {1}'. format(location, renametomp3))
    else:
        os.system('mv {0} {1}'. format(location, renametomp3))


# Driver function.
if __name__ == '__main__':
    main()
