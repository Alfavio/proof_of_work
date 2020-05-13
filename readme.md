![Proof of work](img/logo.jpg)

# Proof of work

In simple words, **proof of work** means:

> I solemnly announce a contest to find a number, which when you insert at the end of the accounting page and you hash this edited page, the resulting hash will begin with twenty zeroes.

In abstraction:

- a *"contest"* is the proof of work
- an *"accounting page"* is a block of the blockchain
- a *"number"* is the nonce

This project produces an example of the proof of work algorithm.

## Requirements

- Python 3
- Multicore CPU is recommended

## Usage

```
usage: main.py [OPTION]

This is a program, that demonstrates an example of proof of work algorithm, with parallel execution.

optional arguments:
        -p, --processes         an integer, specify the number of processes;
                                default 1
        -d, --difficulty        an integer, specify proof of work difficulty;
                                in this case, it is count of zeroes at the start of the wanted hash;
                                default 4
        --help                  display this help and exit

Exit status:
0  if OK,
1  if some problems
```