# coding:utf-8

import pymysql
import random

host = "localhost"
user = "root"
pwd = "lky19990828"
db = "words"


class Dataset:
    def __init__(self):
        self.conn = pymysql.connect(host=host, user=user, password=pwd, database=db)
        self.cursor = self.conn.cursor()
        self.wrong_choice = []
        self.word = ""
        self.right_choice = ""
        self.test()

    def __del__(self):
        self.cursor.close()
        self.conn.close()
        print("连接已断开！")

    def test(self):
        test_text = "select word from words where id = 1"
        self.cursor.execute(test_text)
        result = self.cursor.fetchone()
        if result[0] == 'A':
            print("成功建立连接！")

    def random_select(self):
        random_number = random.randint(1, 15328)
        select_text = "select word,meaning from words where id = %s"
        self.cursor.execute(select_text, random_number)
        select_result = self.cursor.fetchone()

        print(select_result[0])
        print(select_result[1])

        self.word = select_result[0]
        self.right_choice = select_result[1]

    def wrong_choice_select(self):
        self.wrong_choice.clear()
        for i in range(1, 4):
            random_number = random.randint(1, 15328)
            select_text = "select meaning from words where id = %s"
            self.cursor.execute(select_text, random_number)
            select_result = self.cursor.fetchone()
            print(select_result[0])
            self.wrong_choice.append(select_result[0])

    def word_search(self, string):
        pass


if __name__ == '__main__':
    dataset = Dataset()
    dataset.random_select()
    dataset.choice_select()
