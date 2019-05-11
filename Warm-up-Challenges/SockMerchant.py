def sockMerchant(n, ar):
    count_dict = {}
    pair_count = 0
    for i in range(n):
        if ar[i] not in count_dict:
            count_dict[ar[i]] = 1
        else:
            count_dict[ar[i]] += 1
            if count_dict[ar[i]] % 2 == 0:
                pair_count += 1
    return pair_count
