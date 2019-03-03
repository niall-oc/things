# Discover the delimiter in bad data
import argparse


def find_delimiter_indexes(line, delimiter=','):
    """
    returns the index for each occurence of delimiter in a line of data.
    """
    indexes = []
    ind = 0
    while ind > -1:
        ind = line.find(delimiter, ind+1)
        indexes.append(ind)
    return indexes[:-1]


def learn_delimiter(lines, delimiter=' '):
    """
    Analyise a series of lines and determine what indexes never have any data.
    These spaces could be used to delimit the file.
    """
    if lines:
        current_indexes = set(find_delimiter_indexes(lines[0], delimiter=delimiter))
        for line in lines:
            current_indexes = current_indexes & set(find_delimiter_indexes(line, delimiter=delimiter))
        return sorted(current_indexes)
    else:
        raise IndexError('No lines to analyse')


def delimit_indexes(lines, indexes, delimiter=','):
    """
    For each line in lines yield a new line with the indexes marked with the delimiter.
    """
    # For slice replacing have a start and end position for every replace we want to accomplish
    slices = [(indexes[i]+1, indexes[i+1],) for i in range(len(indexes)-1)]
    slices = [(0, indexes[0])] + slices
    return [delimiter.join([line[start:end] for start, end in slices] + [line[indexes[-1]+1:]]) for line in lines]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", dest="infilename", help="The file you want to delimit")
    parser.add_argument("-o", "--outfile", dest="outfilename", help="The newly delimited data")
    parser.add_argument("-l", "--learnwith", dest="learn_with", default=" ",
                        help="The character you want check as a potential delimiter. example -l \" \". quotes are ignored")
    parser.add_argument("-d", "--delimiter", dest="delimiter", help="The new delimiter")
    options, args = parser.parse_args()

    with open(options.infilename, 'r') as infile:
        lines = infile.readlines()
        indexes = learn_delimiter(lines, delimiter=options.learn_with)
        new_lines = delimit_indexes(lines, indexes, delimiter=options.delimiter)

    with open(options.outfilename, 'w') as outfile:
        outfile.write('\n'.join(new_lines))
        outfile.flush()
