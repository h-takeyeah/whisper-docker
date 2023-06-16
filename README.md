# whisper-docker
whisper with docker

:memo: This is a fork of [karaage0703/whisper-docker](https://github.com/karaage0703/whisper-docker)

## Setup
Install Docker.

```sh
$ git clone https://github.com/h-takeyeah/whisper-docker
$ cd whisper-docker
$ docker build -t whisper .
```

## Usage
### Voice recognition with microphone
Execute following command in `whisper-docker` directory.

```sh
$ docker run -it -d -v $(pwd):/workspace/ --net host --name whisper whisper
$ docker exec -it whisper bash
nonroot@hostname:/workspace$ python whisper-server.py
```

Open new terminal and execute following command:

```sh
$ python mic.py
```

> `mic.py` requires [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI).

### Transcribe
Prepare audio file (ex: `input.wav`) and execute following command **in** `whisper-docker` directory.

```sh
$ docker run -it -d -v $(pwd):/workspace/ --net host --name whisper whisper
$ docker exec -it whisper python transcribe.py --model='base' --input_file='input.wav' --output_format='tsv' --language='ja'
```

> DO NOT run this command(line 1 `docker run -it ...`) multiple times which creates a container.
> To create that container again, run `docker kill whisper && docker rm whisper` first, or containers' name may conflict.

## Work with ELAN
[ELAN](https://archive.mpi.nl/tla/elan) can import **csv** or **tsv** formatted transcriptions into eaf(ELAN Annotation Format). A guide page below shows how to do this:

> File > Import > CSV / Tab-delimited Text File....
>
> [ELAN documents / Import and Export options / Import from](https://www.mpi.nl/tools/elan/docs/manual/index.html#Sec_Importing_CSV_Tab-delimited_Text_Files.html)

## Reference
- https://zenn.dev/kento1109/articles/d7d8f512802935
