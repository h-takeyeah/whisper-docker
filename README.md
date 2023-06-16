# whisper-docker
whisper with docker

:memo: オリジナルのリポジトリ [karaage0703/whisper-docker](https://github.com/karaage0703/whisper-docker) と異なり、 Dockerfile ではイメージのサイズを節約するために CPU-only の PyTorch を利用しています。

## セットアップ
Docker Desktop または Docker Engine はインストール済みとします。

次のコマンドでイメージをビルドします:

```sh
$ docker build -t whisper .
```

> イメージのサイズは約 2GB になると見込まれます(推論モデルを含まない容量です)。

## 使い方
### マイクを使った音声認識
`whisper-docker` ディレクトリで次のコマンドを実行します:

```sh
$ docker run -it -d -v $(pwd):/workspace/ --net host --name whisper whisper
$ docker exec -it whisper bash
nonroot@hostname:/workspace$ python whisper-server.py
```

新しい端末を開き、次のコマンドを実行します:

```sh
$ python mic.py
```

> `mic.py` を実行するには [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) がインストールされている必要があります。

### 文字起こし
Prepare audio file (ex: `input.wav`) and execute following command **in** `whisper-docker` directory.
`whisper-docker` ディレクトリ以下に音声ファイルを用意し (例: `input.wav`) 、次のコマンドを `whisper-docker` ディレクトリ**の中で**実行します:

```sh
$ docker run -it -d -v $(pwd):/workspace/ --net host --name whisper whisper
$ docker exec -it whisper python transcribe.py --model='base' --input_file='input.wav' --output_format='tsv' --language='ja'
```

> `docker run -it ...` はコンテナを作成するコマンドです。コンテナを削除する前に再びこのコマンドを実行してコンテナを作成しないようにしてください。
> コンテナを再作成する場合は、まず `docker stop whisper && docker rm whisper` を実行してコンテナを停止・削除してからにしてください。
> そうでないとコンテナ名の衝突でエラーが発生します。なお、今の `docker stop` と `docker rm` は不要なコンテナを削除するために使用します。

## ELAN との組み合わせ
[ELAN](https://archive.mpi.nl/tla/elan) は **CSV** や **TSV** 形式の文字起こしテキストファイルを *EAF (ELAN Annotation Format)* にインポートする機能を持ちます。以下のガイダンスページで操作方法を確認することができます。

> File > Import > CSV / Tab-delimited Text File....
>
> [ELAN documents / Import and Export options / Import from](https://www.mpi.nl/tools/elan/docs/manual/index.html#Sec_Importing_CSV_Tab-delimited_Text_Files.html)

## Reference
- https://zenn.dev/kento1109/articles/d7d8f512802935

---

**日本語** / [English](README-en.md)
