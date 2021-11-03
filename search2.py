"""
３．２に追加してキャラクターリスト(source)をCSVから読み込んで登録できるようにしてみましょう
４．３に追加してキャラクターリスト(source)をCSVに書き込めるようにしてみましょう
"""

import csv

def search_file():
  char_list = []

  with open('char.csv', 'r', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
      char_list.append(row)
  # print(char_list)

  word =input("鬼滅の登場人物の名前を入力してください >>> ")
  flag=0
  """
  csvファイルの内容をchar_listというリストに読み込みましたが、２次元のリストになってしまいました。
  ２次元になったため 「if x in char_list」だけでは検索できず以下のようにfor文で回し検索できるようにしました。
  改善の余地がありそうです。
  """
  for chars in char_list:
    for char in chars:
      if char == word:
        flag=1
        break
  if flag ==1:
    print(f'「{word}」が見つかりました')
  else:
    print(f'「{word}」は見つかりませんでした。リストに追加しファイルに保存します。')
    chars=[]
    chars.append(word)
    char_list.append(chars)
    # print(char_list)
    with open('char.csv', "w", newline="", encoding="utf-8") as csv_file:
      writer = csv.writer(csv_file, delimiter=",")
      """
      csvリストの中身で名前が縦に並ぶようにしたかったので、以下のようにfor文で回しました。
      """
      for chars in char_list:
        writer.writerow(chars)
  
search_file()