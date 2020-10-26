import sys
import os


def main():
    #sys.argv[1]これはpython main.py [文字]の「文字」の部分がsys.argv[1]に代入される。
    #try&except文はもし例外が発生したら○○する。みたいなあらかじめ例外が発生する可能性に備えてコーディングを行う。
    try:
        os.makedirs(sys.argv[1])
        print("新しいディレクトリが作成されました。")
    except FileExistsError:#exceptの隣にはエラーのメッセージをここに
        #ここにはエラーのメッセージが出たときの処理方法を確認してみる。
        print("すでに存在しているディレクトリになります。")

if __name__ == '__main__':
    # モジュールを直接実行した時だけ、実行したいコード
    main()