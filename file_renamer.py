# coding: utf-8

"""
カレントフォルダ直下にある「aaa - bbb 01」形式のフォルダを
「[aaa] bbb 01」形式に変更する
"""

__author__  = 'mystblue'
__version__ = '0.0.1'
__date__    = '2013/11/12'

import os
import re
import Tkinter
import tkMessageBox

class FileRenamer():
    def __init__(self):
        self.counter = 0
        self.pattern = "([^ ]+) - (.+) ([0-9]+)"

    def get_new_name(self, file_name):
        match = re.search(self.pattern, file_name)
        if match:
            new_file_name = "[" + match.group(1) + "] "\
                + match.group(2) + " " + match.group(3)
            return new_file_name
        else:
            return None
    def rename(self):
        """
        カレントフォルダ直下のフォルダをリネームする
        """
        rootDir = "."
        file_list = os.listdir(rootDir)
        for file_name in file_list:
            path = os.path.join(rootDir, file_name)
            # ファイルは処理しない
            if not os.path.isdir(path):
                continue
            # ( や - で始まるフォルダも処理しない
            if file_name.startswith('(') or file_name.startswith('-'):
                continue
            #print file_name
            new_name = self.get_new_name(file_name)
            if new_name:
                #print "process -> " + new_name
                os.rename(file_name, new_name)
                self.counter = self.counter + 1
    
    def show_message(self):
        """
        メッセージを出力する
        """
        root = Tkinter.Tk()
        root.withdraw()

        if self.counter ==0:
            tkMessageBox.showinfo("終了", "フォルダが見つかりませんでした。")
        else:
            tkMessageBox.showinfo("終了", str(self.counter) + "個のフォルダをリネームしました。")

if __name__ == "__main__":
    file_renamer = FileRenamer()
    file_renamer.rename()
    file_renamer.show_message()
