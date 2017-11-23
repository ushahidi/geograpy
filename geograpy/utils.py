import jellyfish


# hat tip http://stackoverflow.com/a/1342373/2367526
def remove_non_ascii(s):
    return "".join(i for i in s if ord(i) < 128)


def fuzzy_match(s1, s2, max_dist=.8):
    return jellyfish.jaro_distance(s1, s2) >= max_dist
