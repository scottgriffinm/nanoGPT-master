import os
import tiktoken
import numpy as np

# input dataset in .txt format
input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(input_file_path, 'r', encoding='utf-8') as f:
    data = f.read()
n = len(data)


def split_data(data_path,n):
    with open(data_path, 'r', encoding='utf-8') as f:
        data = f.read()
    data_len = len(data)
    split_data = []
    for i in range(n):
        split_data.append(data[int(i*(data_len/n)):int((i+1)*(data_len/n))])
    for i in range(len(split_data)):
        with open('split/' + 'input' + str(i) + '.txt', 'w', encoding='utf-8') as f:
            f.write(split_data[i])



train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# train.bin has 301,966 tokens
# val.bin has 36,059 tokens
