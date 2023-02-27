def QuickSort(A, p, r):
    if p < r :
        q = Partition(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)

def Partition(A,p,r):
    x = A[r] # ピボットの選択
    i = p - 1 # 最初の要素の前1つ
    # i=xより小さい値の先頭, j=ピボットとの比較
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
