def jumpingOnTheClouds(li):
    no_of_jumps = i = 0
    while i < len(li):
        if i == (len(li) - 1):
            break
        if (i + 2) <= len(li) and li[i] != 1:
            no_of_jumps += 1
            i += 2
        elif (i + 1) <= len(li) and li[i] != 1:
            no_of_jumps += 1
            i += 1
        else:
            no_of_jumps += 1
            i += 1
    return no_of_jumps
