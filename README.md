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
   `$ git clone https://github.com/Guion-Rem24/jupyter-Docker.git`
2. .envファイルを開き、ユーザ名を入れる 
   
   ```Bash:.env
   user=hogehoge
   
   ```

3. imageのbuild 
   
   ```Bash:terminal
    cd jupyter-Docker
    docker-compose up -d
    
    docker-compose exec ubuntu /bin/bash 
   ```

### 注意事項
- デフォルトでは、最初の実行時にパスワードの設定を求めるようにしています。必要がなければ、Dockerfileの対応箇所をコメントアウトしてください。
- デフォルトでsandboxを、Docker内の/home/{username}/sandboxにマウントしています。必要に応じて修正してください。
- dockerコマンド自体root権限を持っているため、マウントディレクトリ以下は好きにいじれてしまいます。環境を壊さないよう注意してください。\
   またそれに伴って、基本sudoを持ったユーザでログインするようになっています。どうしてもrootでやりたいのであれば、docker-compose.ymlのuser部分をコメントアウトするか、コンテナに入る時にオプションで`--user root`とつけてください。\
   例) `docker-compose exec --user root ubuntu /bin/bash`


### コマンド一覧
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


- `docker ps`\
   現在起動中のコンテナ確認
- `docker ps -a` \
   過去に起動したコンテナも含めて表示
- `docker exec -it [コンテナID or コンテナ名] /bin/bash`\
  コンテナに入る
- `docker images` \
   コンテナ作成に使用したimage一覧

- `docker rm [コンテナID]`\
   コンテナの削除
- `docker rmi [Image ID]`\
   Imageの削除
