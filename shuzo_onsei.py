import time
from pygame import mixer #pygame が必要

class shuzo_onsei:
    def __init__(self, path):
        mixer.init()        #初期化
        mixer.music.load(path)  #音声ファイルのパスを入れて読み込む

    def play(self, numplay):
        mixer.music.play(numplay)  #再生回数を指定して再生