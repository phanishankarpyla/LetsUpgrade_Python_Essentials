for i in range(1,200):
    if i>=4:
        for j in range(2, i):
            if i%j==0:
                break;
        else:
            print(i);
    else:
        print(i);