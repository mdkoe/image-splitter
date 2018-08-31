
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
python3 main.py filename.zip [output_path]
```
![alt text](https://sv1.uphinhnhanh.com/images/2018/08/30/Aug-30-201816-52-43.gif)
# Option
You can custom splice image with after properties
| Property | Values | Default | Preview
| ------- | ------- |------- | -------
| --help |  |  | |
| --log   | True/False | False |
| --png   | True/False | False|
| --jpg   | True/False | True |
| --quality  | 1...100 | 85 |
