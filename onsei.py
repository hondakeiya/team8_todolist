import time
from pygame import mixer #pygame が必要

mixer.init()        #初期化
mixer.music.load("shuzo5.mp3")  #音声ファイルのパスを入れて読み込む
mixer.music.play(1)  #再生回数を指定して再生
time.sleep(5)  #これ入れないと、一瞬で再生されたことになるかも。引数はファイルの秒数に合わせる