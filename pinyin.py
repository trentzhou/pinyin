#!/usr/bin/env python3
import sys

def get_pinyin(input):
    """
    Get an input string, return pinyin format.
    For example, if input is 'hao3', output is 'hǎo'
    :param str input: string
    """
    variants = {
        'a': ['a', 'ā', 'á', 'ǎ', 'à'],
        'o': ['o', 'ō', 'ó', 'ǒ', 'ò'],
        'e': ['e', 'ē', 'é', 'ě', 'è'],
        'i': ['i', 'ī', 'í', 'ǐ', 'ì'],
        'u': ['u', 'ū', 'ú', 'ǔ', 'ù'],
        'ü': ['ü', 'ǖ', 'ǘ', 'ǚ', 'ǜ'],
        'v': ['ü', 'ǖ', 'ǘ', 'ǚ', 'ǜ']
    }
    def tone_radix(c):
        lookup_table = {
            'a': 1,
            'o': 2,
            'e': 3,
            'i': 10,
            'u': 10,
            'v': 10,
        }
        if c in lookup_table:
            return lookup_table[c]
        return 100

    result = []
    for c in input:
        if not c.isdigit():
            result.append(c)
        else:
            # digit!
            index = int(c)
            if index > 4:
                index = 0
            min_pos = 0
            min_radix = 100
            for i in range(len(result)):
                v = tone_radix(result[i])
                if v <= min_radix:
                    min_pos = i
                    min_radix = v
            c = result[min_pos]
            if c in variants:
                result[min_pos] = variants[c][index]
            break
    return ''.join(result)

def main():
    s = " ".join(sys.argv[1:])
    if s:
        # It accepts input from command line arguments
        r = ' '.join([get_pinyin(x) for x in s.split(' ')])
        print(r)
    else:
        # It can also read from stdin
        while True:
            s = sys.stdin.readline()
            if not s:
                break
            r = ' '.join([get_pinyin(x) for x in s.strip().split(' ')])
            print(r)

if __name__ == '__main__':
    main()