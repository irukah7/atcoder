以下を参考にatcoderローカル環境を作成

https://note.com/dev_onecareer/n/n673b1e040956#1b140a32-e7df-4f7e-91b3-a62eb5cb557c

### ログイン設定
atcoder-cli, online-judge-toolsのそれぞれで、AtCoderのユーザーIDとパスワードでログインする。

```
$ acc login
$ oj login https://beta.atcoder.jp/
```

### 問題のダウンロード
```
$ cd ~/Documents/atcoder
$ acc n abc353
```

a, b, c問題をそれぞれのmain.pyで記述していく

### テスト
サンプルケースに対するテストを実行
```
$ cd abc353/a    # 問題ディレクトリに移動
$ ojt
```

### 提出
解答が提出できる状態になったら、`acc s`コマンドで問題を提出する。

提出時に必ず確認文字列の入力が求められるので、`acc s`コマンド後、即座に入力してreturn（Enter）キーを押しておくと、待たされることがない。
（ABCのA問題ならabca、B問題ならabcb、といった具合）

```
$ accs

...
[WARNING] the problem "https://atcoder.jp/contests/abc353/tasks/abc353_a" is specified to submit, but no samples were downloaded in this directory. this may be mis-operation
Are you sure? Please type "abca"
```

## メモ
vi ~/.zshrc の中身
```
python main.pyではなくpython3 main.pyにする
```

* cpythonで提出したい時
  * zshrc or profileに以下を記述する
    * alias accs='acc s -- main.py --language 5055'
* 'oj login https://beta.atcoder.jp'/の時にopensslでエラー（SSLError）が起きた
  * zshrcに以下を記述したら直った
    * export PYENV_ROOT="$HOME/.pyenv"
    * export PATH="$PYENV_ROOT/bin:$PATH"
    * eval "$(pyenv init -)"
* oj -hでpython3.7がno such fileの時(Python3.9.6使っているつもりだが、、pathが正しく通ってない)
  * eval "$(pyenv init --path)"をzshrcに追加すると消えた

## 主原因
* online-judge-toolsをインストールしたのにacc check-ojを実行してonline-judge-tools is not available.と出力された場合の解決方法
  * which ojした時のpathとacc configで出力した時のoj-pathが一致していなかった
    * which oj: /Users/m_hikaru/.pyenv/shims/oj
    * acc config: oj-path: /Users/m_hikaru/.anyenv/envs/pyenv/shims/oj
  * acc configのパスを指定し直す
    * acc config oj-path /Users/m_hikaru/.pyenv/shims/oj