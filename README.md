# Deep Thought
[![CodeFactor](https://www.codefactor.io/repository/github/diicorp95/deep-thought/badge)](https://www.codefactor.io/repository/github/diicorp95/deep-thought)<br>
An artificial intelligence based on multiverse theory and perception principles.

## Algorithm
### The payload
1. Make an random bit array (e.g. `1101...`)
2. Convert the bits to a string
3. Process the resulting string
4. Output it to console

## Usage
On the start, the script waits for user text input. The input is a question that the Deep Thought is being asked about.

## Training
### No automatic training
The neural network does not use machine learning algorithms. Thus, the learning process must be done manually by each user, as each person's perception is different.

### Training file format
A valid training file should be formatted as a JSON structure. However, training files parser does not rely on extensions and etc.
All values in the file should be in the following format:<br>
`"{found_text}": "{output_message}"`, where `{found_text}` — substring that answer parser should find in an answer of neuronet, `{output_message}` — message that answer parser outputs as a message from the Deep Thought.

The default training file is `./{script_name}.trn`, where: `{script_name}` — the filename of script without extension. Usually it is `deep-thought.py`, hence it will look for `deep-thought.trn` in the same directory as the script.

If the given file path is `/dev/null`, then it will just clear the training list.

## Legal
Copyleft of Freedom Level 4 &#127279; [Larry "Diicorp95" Holst](https://github.com/Diicorp95). Licensed under [UNLICENSE license](https://unlicense.org).
