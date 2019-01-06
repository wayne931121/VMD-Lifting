# VMD-Lifting
VMD-Lifting is a fork of 'Lifting from the Deep' that outputs estimated 3D pose data to a VMD file

The authers of 'Lifting from the Deep' are Denis Tome', Chris Russell and Lourdes Agapito.
Please refer 'README-original.md' and http://visual.cs.ucl.ac.uk/pubs/liftingFromTheDeep/
for more information about the original 'Lifting from the Deep'.

This project is licensed under the terms of the GNU GPLv3 license. By using the software,
you are agreeing to the terms of the license agreement (see LICENSE file).

Note: 'shape_predictor_68_face_landmarks.dat', the default trained model for head pose estimation,
was trained on the iBUG 300-W face landmark dataset. And the license for the iBUG 300-W dataset
excludes commercial use. So you should contact Imperial College London to find out if it's OK for
you to use this model file in a commercial product.

## 概要

写真から人のポーズを推定し、VMDフォーマットのモーション(ポーズ)データを出力するプログラムです。
ポーズ推定には Lifting from the Deep (https://github.com/DenisTome/Lifting-from-the-Deep-release)
のプログラムを使用しています。

## お試し

とりあえず使ってみたい方のために [Docker image](https://hub.docker.com/r/errnommd/vmd-lifting) を用意しました。
[Docker](https://www.docker.com/) がインストールされたPCで、例えば C:\test_photo に写真ファイルを置き、
Windows Powershell で次のコマンドを実行します。
写真は全身が写ったものを選んでください。ファイル名は例えば test1.jpg とします。

```
docker run -v c:\test_photo:/vmdl/test -it errnommd/vmd-lifting:latest
```

コンテナとファイルを共有するため、認証のダイアログが出ます。
ファイアウォールを通す設定が必要なこともあります。
なお、Docker imageが約2GBあるので、ダウンロードに時間がかかります。
"root@(文字列):/#" のように書かれたコマンドプロンプトが出たら準備完了です。
下記の手順で VMD-Lifting を実行します(先頭の#は入力しない)。

```
# cd /vmdl/applications
# python3 vmdlifting.py ../test/test1.jpg ../test/test1.vmd
```

次のようなメッセージが表示され、C:\test_photo に test1.vmd が作られます。
この VMD ファイルを MMD に読ませましょう。

```
pose estimation start
...
(略)
...
frame_num:  0
root@.......:/vmdl/applications#

```

終了するときは exit と入力します。

以上のように Docker で使い続けることもできますが、Docker版はGPUを使わない設定になっているので遅いです。
本格的に使用したい場合は、下記の手順でインストールを行い、GPUを有効にして使うことをお勧めします。

## インストールに必要なもの
- python (3.x)
- [Tensorflow](https://www.tensorflow.org/)
- [OpenCV](http://opencv.org/)
- python-tk (Tkinter)
- PyQt5
- dlib

Ubuntu や Debian GNU/Linux の環境では、rootになって下記のコマンドを実行すると必要なものが揃います。

```
# apt-get install python3-pip
# pip3 install tensorflow-gpu
# apt-get install python3-opencv
# apt-get install python3-tk
# apt-get install python3-pyqt5
# apt-get install cmake
# pip3 install dlib
```

Windowsの場合は次の手順で必要なものをインストールします。

- cygwin をインストール: https://cygwin.com/install.html

- https://www.tensorflow.org/install/install_windows に従って、CUDA、cuDNN、Python 3.6 をインストール

- cygwin の pythonでなく、上記でインストールしたpythonを使うように環境変数PATHを設定

- tensorflowをpipでインストール

`$ pip install  tensorflow-gpu`

- OpenCVをインストール

`$ pip install opencv-python`

- PyQt5をインストール

`$ pip install PyQt5`

- dlibをインストール

`$ pip install dlib`

## 準備
- まず setup.sh を実行します。このスクリプトは必要なデータを取得し、外部ユーティリティをインストールします。
- (次に、Lifting from the Deep 本体の動作を確認したい場合は、application ディレクトリで demo.py を実行します。)

- dlib + OpenCVによるHead Pose Estimation(頭部姿勢推定)を行う場合は、
http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 をダウンロードし、
展開してできたファイル shape_predictor_68_face_landmarks.dat を applications/predictor/ に置きます。

```
$ mkdir applications/predictor
$ cd applications/predictor
$ wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
$ bunzip2 shape_predictor_68_face_landmarks.dat.bz2
```

## 使用方法

cd application

./vmdlifting.py IMAGE_FILE VMD_FILE [POSITION_FILE]

- IMAGE_FILE: 入力元画像/動画ファイル(JPEG, PNG, MP4など)
- VMD_FILE: 出力先VMDファイル
- POSITION_FILE(オプション): 関節の位置を出力するテキストファイル。デバッグ用。

使用例:

./vmdlifting.py photo.jpg estimated.vmd

## Lifting from the Deep について

Lifting from the Deep は、畳み込みニューラルネットワーク(CNN)を用いて、
単一のRGB画像から3Dのポーズ推定を行う手法(の論文)および、それを実装したプログラムです。
著者は Denis Tome', Chris Russell, Lourdes Agapito です。
詳しくはプロジェクトのWebページ ( http://visual.cs.ucl.ac.uk/pubs/liftingFromTheDeep/ )
の論文や動画を参照してください。

## ライセンスについて
(はじめに英語で書いたとおり)GNU GPLv3 licenseです。詳しくはLICENSEファイルを読んでください。
なお、顔の向きを推定するのに使う学習済みモデル shape_predictor_68_face_landmarks.dat は、
学習に用いられた iBUG 300-W データセットが商用利用を許可されていません。
もし商用利用する場合は Imperial College London に許諾を得るか、別の学習済みモデルを用意してください。

## 参考文献

D. Tome, C. Russell and L. Agapito. Lifting from the Deep: Convolutional 3D Pose Estimation
from a Single Image. In IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017
