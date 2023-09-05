# Calculate a similarity score between a generated sample and the dataset it was trained on.
# similarity score = number of lines in the sample that are also in the training/validation datasets / total number of lines in the sample
# *** excluding empty lines and song section markers (e.g. [Chorus], [Verse], etc.) as well as separators (e.g. '----------------')

def similarity_score(sample, dataset):
    sample = sample.lower()
    dataset = dataset.lower()
    sampleLines = sample.splitlines()
    length = len(sampleLines)
    i = 0
    while i < length:
        if sampleLines[i] == '':
            sampleLines.pop(i)
            length -= 1
            continue
        elif sampleLines[i].startswith('['):
            sampleLines.pop(i)
            length -= 1
            continue
        elif sampleLines[i].startswith('\n'):
            sampleLines.pop(i)
            length -= 1
            continue
        elif sampleLines[i].startswith('----------------'):
            sampleLines.pop(i)
            length -= 1
            continue
        i += 1
    count = 0
    for i in range(len(sampleLines)):
        if sampleLines[i] in dataset:
            count += 1
            print(sampleLines[i])
    score = count / len(sampleLines)
    return score

