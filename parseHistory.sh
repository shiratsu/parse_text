#!/bin/sh
#
# 応募者処理sh
# PDFがパスワードかかってたら解除
# 日本語もう舞妓と処理して、テキストファイルに保存
# そのテキストをパースして特徴を抜き出す(python)
#

DATE=date '+%Y%m%d'

if [ $# -eq 1 ]; then
  pdftotext -layout $1 history_$DATE.txt
fi
