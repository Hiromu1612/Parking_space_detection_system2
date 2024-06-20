# ベースイメージとしてtensorflowの公式イメージを使用
FROM sonoisa/deep-learning-coding:pytorch1.12.0_tensorflow2.9.1

# 作業ディレクトリを設定
WORKDIR /app

# requirements.txtをコンテナにコピー
COPY requirements.txt /app/

# requirements.txtからパッケージをインストール
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ホストマシンの全てのファイルをコンテナ内の /app ディレクトリにコピー
COPY . /app

# コンテナ起動時に実行するデフォルトのコマンド
CMD ["python"]