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
            if i.endswith('S') and len(i) != 1:
                size_s.append(i)
                sizes_str.remove(i)
            if i.endswith('L') and len(i) != 1:
                size_l.append(i)
                sizes_str.remove(i)
        size_s = sorted(size_s, key=len, reverse = True)
        size_l = sorted(size_l, key=len)
                
        for i in requested_size_str:
            if i == 'S':
                if 'M' in sizes_str:
                    requested_size_str.remove(i)
                    sizes_str.remove('M')
                if 'L' in sizes_str:
                    requested_size_str.remove(i)
                    sizes_str.remove('L')
                if len(size_l) != 0:
                    requested_size_str.remove(i)
                    size_l.pop(0)
                else:
                    print('No')
            elif i == 'M':
                if 'L' in sizes_str:
                    requested_size_str.remove(i)
                    sizes_str.remove('L')
            
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
            
            elif i.endswith('S'):
                if len(size_s) != 0:
                    requested_size_str.remove(i)
                    size_s.pop(0)
                else:
                    print('No')
            
            elif i.endswith('L'):
                if len(size_l) != 0:
                    requested_size_str.remove(i)
                    size_l.pop(0)
                else:
                    print('No')
            

        if len(requested_size_str) == 0:
            print('Yes')
            
