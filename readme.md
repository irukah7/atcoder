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