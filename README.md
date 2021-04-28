# Docker環境構築のテンプレート
### 構造

```Bash:構造
.
├── README.md
├── build
│   └── Dockerfile
├── docker-compose.yml
└── sandbox
    ├── jupyter_notebook_config.py
    └── start_jupyter.sh
```

### 手順

1. リポジトリのクローン \
   
   ```Bash
   $ git clone https://github.com/Guion-Rem24/jupyter-Docker.git
   ```

2. .envファイルを開き、ユーザ名、jupyterの設定を入力
   
   ```Bash:.env
   user=hogehoge
   jupyter_passwd=''
   jupyter_port=8888
   jupyter_work_dir=fugafuga
   ```

   Jupterのパスワードは空欄（`''`）でも起動できます。

3. imageのbuild 
   
   ```Bash
   $ cd jupyter-Docker
   $ docker-compose up -d
    
   $ docker-compose exec ubuntu /bin/bash 
   ```

### 注意事項
- デフォルトでは、最初の実行時にパスワードの設定を求めるようにしています。必要がなければ、Dockerfileの対応箇所をコメントアウトしてください。
- デフォルトでは、ホストのsandboxを、Docker内の`/home/{username}/{jupyter_work_dir}`にマウントしています。必要に応じて修正してください。
- dockerコマンド自体root権限を持っているため、マウントディレクトリ以下は好きにいじれてしまいます。環境を壊さないよう注意してください。\
   またそれに伴って、基本sudoを持ったユーザでログインするようになっています。どうしてもrootでやりたいのであれば、docker-compose.ymlのuser部分をコメントアウトするか、コンテナに入る時にオプションで`--user root`とつけてください。\
   例) `docker-compose exec --user root ubuntu /bin/bash`


### コマンド一覧
<details><summary> <strong>Docker環境 </strong></summary>

- `docker-compose up`\
   コンテナの起動
- `docker-compose up -d` \
   バックグラウンドで起動
- `docker-compose up -d --build`\
   Imagemのビルドを実行し、コンテナをバックグラウンドで起動
- `docker-compose exec [service] /bin/bash` \
  実行中のコンテナに入る。serviceはデフォルトでubuntu。（docker-compose.yml参照）
- `docker-compose stop`\
   起動中のコンテナを止める
- `docker-compose down`\
   起動中のコンテナを止め、コンテナを破棄する
- `docker-compose build`\
   ビルドだけ行う

<br />

- `docker ps`\
   現在起動中のコンテナ確認
- `docker ps -a` \
   過去に起動したコンテナも含めて表示
- `docker exec -it [コンテナID or コンテナ名] /bin/bash`\
  コンテナに入る
- `docker images` \
   コンテナ作成に使用したimage一覧

<br />

- `docker rm [コンテナID]`\
   コンテナの削除
- `docker rmi [Image ID]`\
   Imageの削除

- `docker rmi $(docker images -f "dangling=true" -q)` \
  imageのビルドの失敗/pullの失敗等により、`docker images`で出力されたimageの中に`<none>`というタグの使われないimageが存在することがあります。これを一括削除するコマンドです。\
  なお、docker APIのバージョンが1.25以上の場合は以下のコマンドと同義です。\
  `docker image prune` \
  Docker APIのバージョンは以下のコマンドで確認できます。\
  
  ```Bash
  $ docker version | grep -i api
   API version:       1.41
  API version:      1.41 (minimum version 1.12)
  ```


</details>

<details><summary> <strong>Jupyterの操作</strong></summary>

- `./start_jupyter.sh` \
  Jupyter notebookの起動
- `jupyter notebook list` \
  起動しているJupyterの一覧表示
- `jupyter notebook stop $JUPYTER_PORT` \
  `./start_jupyter.sh`で起動したJupyterの停止
  `$JUPYTER_PORT`のデフォルトは8888なので、置き換えてもよい \
  このコマンドを実行してもエラーを吐いて停止しない場合は、以下のコマンドで停止できる。
  しかし、<strong>すべてのJupterを停止すること</strong>になるので注意が必要。<br /> 
  - `pkill jupyter`

<br />

- Jupyterが起動しない等の問題があったら、コンテナ内の`/home/{username}/.jupyter/jupyter.log`に直近のlogを保持しています。確認して対応してください。

</details>