# coding: UTF-8

import sys # モジュール属性 argv を取得するため
import MeCab
import re
import pprint

# めかぶと辞書配列の定義
mecab = MeCab.Tagger('mecabrc')
aryNoun = []
aryFixNoun = []

# ワード配列にセットしていく
def getwords(content):
    # print("tesjjjjjjjjjjjtets")
    content = content.strip()
    # node = mecab.parseToNode(content)
    # print("----------------------------")
    # dump(node)
    # print("----------------------------")
    # while node:
    #     pos0 = node.feature.split(",")[0]
    #     pos1 = node.feature.split(",")[1]
    #     # if pos0 == "名詞" and pos1 == "一般":
    #         # print(node.text)
    #         # aryWord.append(node.text)
    #         # print(node.surface)
    #         # print(node.feature)
    #     node = node.next
    print(content)
    i=0
    analyzetext = mecab.parse(content)
    aryNode = re.split("[\t,]",analyzetext)
    print(aryNode)
    # node = mecab.parseToNode(content)
    # while node:
    #
    #     if i == 10:
    #         break
    #
    #     # node = n.feature.split(',');
    #     # dump(node)
    #     print(node.feature)
    #     # print("-----------------------------")
    #     # print(node[0])
    #     # print(node[1])
    #     # print(node[2])
    #     # print(node[3])
    #     # print("-----------------------------")
    #     # print(node)
    #     #
    #     # if node[0] == '名詞' and node[1] == '一般':
    #     #     aryNoun.append(node[6])
    #     # elif node[0] == '名詞' and node[1] == '固有名詞':
    #     #     # if True:
    #     #     aryFixNoun.append(node[6])
    #
    #     i+=1


# １行ずつ読み込んでパースしていく
def readFile(filename):
    for line in open(filename, 'r'):
        # print line
        getwords(line)

def dump(obj):
  for attr in dir(obj):
    print("obj.%s = %s" % (attr, getattr(obj, attr)))

if __name__ == "__main__":
    argvs = sys.argv  # コマンドライン引数を格納したリストの取得
    # getwords("hiratsukatest")
    readFile(argvs[1])
    # getwords("hiratsukatest")

    text = "私は、PHPとswiftとRubyとDjangoを使ったことがあります"
    print(mecab.parse(text))

    text = "現在はTech::CampにてRuby on Railsでのwebアプリケーションの学習・制作"
    print(mecab.parse(text))


    # print(aryNoun)
    # print(aryFixNoun)
