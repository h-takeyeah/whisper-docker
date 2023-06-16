#!/usr/bin/env python
import argparse
import os
from dataclasses import asdict
import whisper


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--model', type=str, default='base')
    parser.add_argument('--input_file', type=str, default='input.wav')
    parser.add_argument('--output_format', type=str, default='tsv')
    parser.add_argument('--language', type=str, default='ja')

    args = parser.parse_args()
    return args


def main():
    args = get_args()

    model_name = args.model
    input_file = args.input_file
    output_format = args.output_format
    language = args.language

    output_dir = 'transcript'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    writer = whisper.utils.get_writer(output_format, output_dir)

    whisper_model = whisper.load_model(model_name, download_root='./')
    decode_options = whisper.DecodingOptions(
        language=language,
        best_of=5,
        beam_size=5,
        patience=1.0,
    )
    result = whisper_model.transcribe(
        input_file,
        verbose=False,
        compression_ratio_threshold=2.4,
        no_speech_threshold=0.6,
        **asdict(decode_options)
    )

    writer(result, input_file)


if __name__ == "__main__":
    main()
