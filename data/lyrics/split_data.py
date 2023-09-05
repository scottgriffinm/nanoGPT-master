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
