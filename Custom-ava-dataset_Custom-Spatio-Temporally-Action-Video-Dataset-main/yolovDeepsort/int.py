
# F4 = r"D:\_PT22\gt_truth\14_ocsort.txt"
# F3 = r"D:\_PT22\gt_truth\14_ds.txt"
# F1 = r"D:\_PT22\gt_truth\14_oc.txt"
# F2 = r"D:\_PT22\gt_truth\14_byte.txt"

# 2 视频
def int_to_int2(a):
    if a == 0:
        a = 0
    elif a == 1:
        a = 2
    elif a == 2:
        a = 1
    elif a == 3:
        a = 7
    elif a == 4:
        a = 4
    elif a == 5:
        a = 3
    elif a == 6:
        a = 5
    elif a == 7:
        a = 6
    return a

# 11 视频
def int_to_int11(a):
    if a == 0:
        a = 0
    elif a == 1:
        a = 1
    elif a == 2:
        a = 4
    elif a == 3:
        a = 3
    elif a == 4:
        a = 6
    elif a == 5:
        a = 5
    elif a == 6:
        a = 2
    elif a == 7:
        a = 7
    return a

# 14 视频
def int_to_int14(a):
    if a == 0:
        a = 2
    elif a == 1:
        a = 0
    elif a == 2:
        a = 5
    elif a == 3:
        a = 1
    elif a == 4:
        a = 3
    elif a == 5:
        a = 7
    elif a == 6:
        a = 4
    # elif a == 7:
    #     a = 6
    return a

# 18视频
def int_to_int18(a):
    if a == 0:
        a = 2
    elif a == 1:
        a = 3
    elif a == 2:
        a = 6
    elif a == 3:
        a = 1
    elif a == 4:
        a = 4
    elif a == 5:
        a = 5
    elif a == 6:
        a = 0
    elif a == 7:
        a = 7
    return a

