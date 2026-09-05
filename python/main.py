# generator practice

def sliding_window_pairs(stream):
    
    iterator = iter(stream)
    
    try:
        perv = next(iterator)
    except Exception as e:
        raise e
        print('Encoutnered error while trying to assig perv!')
        return 0
        
    for current in iterator:
        yield (perv, current)
        perv = current
        
# Testing program:
stream_range = (x for x in range(10000000))
gen_obj = sliding_window_pairs(stream_range)
for i in range(10):
    print(next(gen_obj))

