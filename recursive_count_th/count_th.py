'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) < 2:
        return 0

    if (word[:2]) != 'th':
        word = word[1:]
        return count_th(word)
    else:
        word = word[2:]
        return count_th(word) + 1
