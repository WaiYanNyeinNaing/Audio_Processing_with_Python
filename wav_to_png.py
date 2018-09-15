import csv
import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
import time
from time import gmtime, strftime


    
DIRNAME = 'gb\\fold1\\'
#OUTPUTFILE = r'c:\path\to\outputfiledir\outputfile.csv'

def get_file_paths(dirname):
    file_paths = []  
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  
    return file_paths    


def main():
    count = 0
    files = get_file_paths(DIRNAME)                 # get all file-paths of all files in dirname and subdirectories
    for file in files:                              # execute for each file
        (filepath, ext) = os.path.splitext(file)    # get the file extension
        file_name = os.path.basename(file)          # get the basename for writing to output file
        if ext == '.wav':                           # only interested if extension is '.wav'
            y, sr = librosa.load(file)
            plt.subplot(1, 1, 1)
            #librosa.display.waveplot(y, sr=sr)
            #plt.title('Stereo')
            y_harm, y_perc = librosa.effects.hpss(y)
            librosa.display.waveplot(y_harm, sr=sr, alpha=0.25)
            librosa.display.waveplot(y_perc, sr=sr, color='r', alpha=0.5)
            date = strftime("%d-%b-%Hhr-%Mmin-%Ssec ", gmtime())
            plt.savefig('spectrograms/' + date + '.png')
            count += 1
            print(count)
            plt.close()
              

if __name__ == '__main__':
    main()
