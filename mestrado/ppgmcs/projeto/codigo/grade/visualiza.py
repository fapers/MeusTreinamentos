def exibe_gradefx1(t, d, h, gr, hca):

    print('\t', end="\t")

    for i in range(len(t)):
        print(f't{i+1}', end="\t")

    print("FX1")

    for i in range(len(d)):
        print(f'D{i+1}', end="\t")
        for j in range(len(h)):
            if(j == 0):
                print(f'H{j+1}', end="\t")
            else:
                print(f'\tH{j+1}', end="\t")
            for k in range(len(t)):
                print(f'p{gr[i][j][k]+1:0>2}', end="\t")
            print(f'{hca[i][j]}')

        print("")
