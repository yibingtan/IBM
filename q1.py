import numpy

n = input()
sizes_str = input().split(' ')
request = input()
requested_size_str = input().split(' ')

size_s = [] 
size_l = []
common = np.intersect1d(sizes_str, requested_sizes_str)

if request > n:
    print('No')

else:
    for i in range(len(common)):
        # remove
        sizes_str.remove(common[i])
        requested_size_str.remove(common[i])
        for i in sizes_str:
            if i.endswith('S'):
                size_s.append(i)
                sizes_str.remove(i)
            if i.endswith('L'):
                size_l.append(i)
                sizes_str.remove(i)
        size_s = sorted(size_s, key=len)
        size_l = sorted(size_l, key=len)
                
        for i in requested_size_str:
            if i == 'S':
                if 'M' in sizes_str:
                    requested_size_str.remove(i)
                    sizes_str.remove('M')
                if 'L' in size_l:
                    requested_size_str.remove(i)
                    sizes_str.remove('L')
                if len(size_l) != 0:
                    requested_size_str.remove(i)
                    size_l.pop(0)
                else:
                    print('No')
            elif i == 'M':
                if len(size_l) != 0:
                    requested_size_str.remove(i)
                    size_l.pop(0)
                else:
                    print('No')

            elif i == 'L':
                if len(size_l) != 0:
                    requested_size_str.remove(i)
                    size_l.pop(0)
                else:
                    print('No')

        if len(requested_size_str) == 0:
            print('Yes')
            

    
    
    


