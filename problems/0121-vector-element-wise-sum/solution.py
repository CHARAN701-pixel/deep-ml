def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
   if len(a) != len(b) :
    return -1
   else:
    sum_list=[]
    for i in range(len(a)):
        total=a[i]+b[i]
        sum_list.append(total)
    return sum_list # Return the element-wise sum of vectors 'a' and 'b'.
    # If vectors have different lengths, return -1.
    pass