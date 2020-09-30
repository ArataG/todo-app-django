#!/bin/bash

# souceコマンドを利用(指定したファイルの内容をそのままコマンドラインに流したように実行される)
# source ./setalias.sh
#で設定できる．

source ./myvenv/bin/activate

# django project alias setup 

projectpath="/Users/sugiharashin/Documents/todoApp"
projecturl="http://127.0.0.1:8000/"

# cd project dir
alias p='cd "$projectpath"'

# op 
alias op='open "$projecturl"'

# run webserver
alias run='python "$projectpath"/manage.py runserver'
