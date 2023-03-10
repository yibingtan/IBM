import numpy

n = input()
sizes_str = input().split(' ')
request = input()
requested_size_str = input().split(' ')

common = np.intersect1d(sizes_str, requested_sizes_str)

if request > n:
    print('No')

else:
    for i in range(len(common)):
        # remove
        sizes_str.remove(common[i])
        requested_size_str.remove(common[i])

        for i in requested_size_str:
            if i == 'S':
                if 'M' in sizes_str:
                    requested_size_str.remove(i)
                    sizes_str.remove('M')
                if 'L' in sizes_str:
                    requested_size_str.remove(i)
                    sizes_str.remove('L')

                else:
                    print('No')
            elif i == 'M':
                if 'L' in sizes_str:
                    requested_size_str.remove(i)
                    sizes_str.remove('L')

                else:
                    print('No')

            elif i == 'L':
                if 'XL' in sizes_str:
                    requested_size_str.remove(i)
                    sizes_str.remove('XL')
                    
                else:
                    print('No')

        if len(requested_size_str) == 0:
            print('Yes')
            

    
    
    


