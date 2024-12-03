# File Manipulator Program

このプログラムは、指定したファイルに対して様々な操作を行うツールです。以下の操作がサポートされています。

## 操作

- **reverse**: ファイルの内容を反転させて新しいファイルに保存
- **copy**: ファイルの内容をコピーして新しいファイルに保存
- **duplicate**: ファイルの内容を指定された回数だけ重複させて追記
- **replace**: ファイル内の文字列を別の文字列に置き換え

## 使い方

プログラムを実行するには以下の形式でコマンドライン引数を指定してください。


- **reverse**
```bash
python file_manipulator.py reverse input.txt output.txt
```
- **copy**
```bash
python file_manipulator.py copy input.txt output.txt
```
- **duplicate**
```bash
python file_manipulator.py duplicate input.txt n
```
- **replace**
```bash
python file_manipulator.py replace input.txt old_string new_string
```

#### 使用技術
<p style="display: inline">
<img src="https://img.shields.io/badge/-Linux-212121.svg?logo=linux&style=popout">
<img src="https://img.shields.io/badge/-Python-FFC107.svg?logo=python&style=popout">
</p>

&nbsp;

## 環境構築
### 開発環境
| OS・言語・ライブラリ | バージョン |
| :------- | :------ |
| Ubuntu | 22.04.4 LTS |
| Python | 3.10.12 |

&nbsp;
