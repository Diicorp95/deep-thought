#!/usr/bin/python3

"""
    Program Name: Deep Thought (artifical intellegence)
    Version     : 0.5.2.1
    Author      : Diicorp95
    License     : UNLICENSE license
"""

import random       # Random data
import json         # Storing training_data
import sys          # Reading arguments to script
import os           # Validating file paths
import unicodedata  # Cleaning input - Adding Unicode symbols to range
import re           # Cleaning input - RegEX
import itertools    # Cleaning input - Making a chain

# Constants
TEXTS = [
    """
      ____
     / __ \\ ___   ___    ____
    / / / // _ \\ / _ \\  / __ \\
   / /_/ //  __//  __/ / /_/ /
  /_____/ \\___/ \\___/ / .___/
        ______ __    /_/                   __     __
       /_  __// /_   ____   __  __ ____ _ / /_   / /_
        / /  / __ \\ / __ \\ / / / // __ `// __ \\ / __/
       / /  / / / // /_/ // /_/ // /_/ // / / // /_
      /_/  /_/ /_/ \\____/ \\__,_/ \\__, //_/ /_/ \\__/
                                /____/

 > Deep Thought - artifical intellegence
 - Version 0.5.2.1
 > Code was written by Larry Holst (Diicorp95)
 - UNLICENSE license
    """,
    """
 * Training data loaded from {0:s}
 - {1:d}/{2:d} entries
 - {3:.3g} KB
    """,
    """
 * File {0:s} is missing
    """,
    """
 * Cleared training data
    """,
    """
 > Help
 # Arguments
   Options: [ [-h | --help | /h|  /?] | [-t|  --training| /t] [filename] ]
   -h                 Displays this message
   --help
   /h
   /?
   -t                 Load a training file. Default: %script_basename%.trn
   --training
   /t

   Additional options at the end: [ [-inf | --infinite | /i] ]
   -inf               Infinite dialog (until Ctrl-C or empty input)
   --infinite
   /i

 # Training
   # No automatic training
   The neural network does not use machine learning algorithms. Thus, the
   learning process must be done manually by each user, as each person's
   perception is different.

   # Training file format
   A valid training file should be formatted as a JSON structure. However,
   training files parser does not rely on extensions and etc. All values in the
   file should be in the following format:
   `"{found_text}": "{output_message}"`, where: `{found_text}` — substring that
   answer parser should find in an answer of neuronet, `{output_message}` —
   message that answer parser outputs as a message from the Deep Thought.

   The default training file is `./{script_name}.trn`, where: `{script_name}` —
   the filename of script without extension. Usually it is `deep-thought.py`,
   hence it will look for `deep-thought.trn` in the same directory as the
   script.

   If the given file path is `/dev/null`, then it will just clear the training
   list.

 # Usage
   On the start, the script waits for user text input. The input is a question
   that the Deep Thought is being asked about.
""",
]
FILE_EXTENSION = ".trn"
CLEAN_TRAINING = "/dev/null"
POSSIBLE_ARGS = {
    "--help": 4,
    "-h": 4,
    "/?": 4,
    "/h": 4,
    "--training": 10,
    "-t": 10,
    "/t": 10,
}

# Classes
class Training:
    def __init__(self, d_list):
        self.d_list = d_list

    def update(self, d_list):
        self.d_list = d_list


# Functions
def text_print(index, *format_data):
    form = TEXTS[index]
    if format_data:
        form = form.format(*format_data)
    print(form)


def clean_string(dirty):
    achars = (chr(i) for i in range(sys.maxunicode))
    cats = {"Cc"}
    _ = [c for c in achars if unicodedata.category(c) in cats]
    ctrl_chars = "".join(_)
    _ = map(chr, itertools.chain(range(0x00, 0x20), range(0x7F, 0xA0)))
    ctrl_chars = "".join(_)
    ctrl_char_re = re.compile("[%s]" % re.escape(ctrl_chars))
    return ctrl_char_re.sub("", dirty)


def process_path_info(filepath = False):
    if isinstance(filepath, bool) and filepath == False:
        return os.path.splitext(sys.argv[0])[0] + FILE_EXTENSION
    elif isinstance(filepath, str):
        try:
            if not os.path.splitext(filepath)[1] == FILE_EXTENSION:
                res = os.path.splitext(sys.argv[0])[0] + FILE_EXTENSION
            else:
                res = filepath
        except IndexError:
            res = os.path.splitext(sys.argv[0])[0] + FILE_EXTENSION
        return res
    return ""


def load_json():
    filepath = ""
    empty_list = None
    try:
        if (sys.argv[2])[0:9] == CLEAN_TRAINING:
            empty_list = True
            train.update({})
    except IndexError:
        empty_list = False
    try:
        filepath = process_path_info(sys.argv[2])
    except IndexError:
        filepath = process_path_info()
    basename = os.path.basename(filepath)
    if not empty_list:
        if os.path.exists(filepath) and os.path.isfile(filepath):
            with open(filepath) as f:
                try:
                    x = json.load(f)
                    train.update(x)
                except UnicodeDecodeError:
                    return 4
            entries = len(list(train.d_list.keys()))
            r_entries = len(list(x.keys()))
            kibis = round(os.path.getsize(filepath) / 1024, 3)
            return [0, basename, entries, r_entries, kibis]
        return [5, basename]
    return [100]


def args_work():
    try:
        x = load_json()
        if type(x) == list and x[0] == 0:
            return x
    except FileNotFoundError:
        pass
    except IOError:
        pass
    except IndexError:
        pass
    try:
        argc = len(sys.argv)
        if argc > 0:
            _ = sys.argv[1]
            try:
                x = POSSIBLE_ARGS.get(_.lower())
            except IndexError:
                return 0
            if x > -1:
                if x < 10:
                    return x << 4
                return load_json()
            return 0
    except IOError:
        return 1
    except UnicodeDecodeError:
        try:
            _ = process_path_info()
            return [4, _]
        except IndexError:
            return [4, None]
    except IndexError:
        return 0


def set_seed_from_user(the_input):
    if isinstance(the_input, str) and the_input:
        proc_input = 0
        for i in the_input:
            proc_input = (proc_input << 1) + (ord(i) % 16)
        nseed = proc_input
        if len(the_input) > proc_input:
            for i in range(0, len(the_input)):
                j = proc_input + i
                try:
                    nseed &= chr(the_input[j]) % 1
                except TypeError:
                    break
        random.seed(nseed)
        return 0
    return 1


def nth_keyname(dic, n):
    try:
        _ = list(dic.keys())[n]
        if isinstance(_, str):
            return _
        return False
    except IndexError:
        return False


def random_bit_array(length):
    the_array = []
    x = [1] * 2
    for i in range(0, length):
        the_array.append(int(bin(x[0] * x[1])[2:]))
        x[1] += random.getrandbits(1)
        x[0] = ((x[0] << 2) & (x[0] + 1)) | random.getrandbits(1)
    return the_array


def parse_raw(info):
    the_string = ""
    switch = train.d_list
    for i, key in enumerate(switch):
        key = nth_keyname(switch, i)
        if not _ is False:
            if info.find(_) > -1:
                return switch[_]
    return info


if __name__ == "__main__":
    train = Training({})

    for i, j in enumerate(TEXTS):
        TEXTS[i] = j.rstrip()
    text_print(0)

    _ = args_work()
    if type(_) == list:
        if _[0] == 0:
            text_print(1, _[1], _[2], _[3], _[4])
        elif _[0] == 5:
            try:
                if not _[2] == True:
                    raise BaseException
            except BaseException:
                text_print(2, _[1])
        elif _[0] == 6:
            text_print(4, _[1])
        elif _[0] == 100:
            text_print(3)
    else:
        if _ >= 16:
            cor_text = _ >> 4
            text_print(cor_text)
            raise SystemExit

    while True:
        while True:
            try:
                user_i = input("\nUser - ")
            except KeyboardInterrupt:
                raise SystemExit
            if not user_i:
                raise SystemExit
            break
        user_i = user_i.strip().upper()
        set_seed_from_user(user_i)
        print("Computer - Hmm...")

        accumulator = ""
        for i, j in enumerate(random_bit_array(2 ** 8)):
            accumulator += str(j)
            accumulator = "".join(random.sample(accumulator, len(accumulator)))

        for n in range(0, 2 ** 3):
            thought = ""
            for i in range(0, len(accumulator) % 16):
                thought += chr(int(str(accumulator)[i : i + 8], 2))
            output = clean_string(thought.strip())
            if not output:
                output = "Nothing"
            else:
                output = parse_raw(str(output))
            if not output == "Nothing":
                break

        print("Computer -", output)
