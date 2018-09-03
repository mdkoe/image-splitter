
# Image-splitter

## インストール方法
[Python3](https://www.python.org/downloads/) (3.7.0)
- MacOS
```
brew install python3
```
[ImageMagick](https://www.imagemagick.org/script/download.php)
- MacOS
```
brew update
brew install imagemagick
```

## Usage

コンマンドに以下の通りに実行して下さい
```
python3 main.py [option] filename.zip [output_path]
```
![alt text](https://sv1.uphinhnhanh.com/images/2018/08/30/Aug-30-201816-52-43.gif)
- output_path
  分轄の結果を保存するフォルダのパスです。
# Option
-  `--log`:　コマンドに分割状況を表示するかどうか価値

```
python3 main.py --log filename.zip
```
- `--png`,`--jpg`:　分割した画像の形式。`--png`と`--jpg`一緒に使う場合ブログラムが最終の価値を使います。使わない場合は画像の形式が`jpg`を分割します。

```
python3 main.py --png filename.zip
```

- `--quality`:　`--jpg`を使う場合は分割した`--jpg`画像の品質。`--quality`使わない場合は`--quality`の価値は`85`です。

```
python3 main.py --jpg --quality 60 filename.zip
```
