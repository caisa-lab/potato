import json
from argparse import ArgumentParser
from pathlib import Path

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('--input-file', type=str, required=True)
    parser.add_argument('--output-file', type=str, required=True)
    parser.add_argument('--sample', type=int)

    args = parser.parse_args()

    input_file = Path(args.input_file)
    output_file = args.output_file
    sample = args.sample

    with open(input_file) as f:
        lines = f.readlines()
        if sample < len(lines):
            lines = lines[:sample]

    with open(output_file, "w") as outfile:
        for idx, line in enumerate(lines):
            line = json.loads(line)
            entry = {"id": f'{input_file.name}_{idx}', "text": line['prompt']}
            print(json.dumps(entry), file=outfile)
