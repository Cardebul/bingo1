

def calc(bingo, mod):
    flag = False
    progress = 0
    start = 1
    start_2 = 1
    end = mod + 1
    val = []
    for i in range(mod):
        # row
        for j in range(start, end):
            val.append(bingo.__dict__[f'field{j}'])
        if sum(val) == mod:
            progress += 1
        val.clear()
        # col
        for j in range(start_2, (mod**2)+1, mod):
            val.append(bingo.__dict__[f'field{j}'])
        if sum(val) == mod:
            progress += 1
        start_2 += 1
        start = end
        end += mod
        val.clear()
    # diag
    for i in range(1, (mod**2)+1, mod+1):
        val.append(bingo.__dict__[f'field{i}'])
    if sum(val) == mod:
        progress += 1
    val.clear()
    for i in range(mod, (mod**2)-1, mod-1):
        val.append(bingo.__dict__[f'field{i}'])
    if sum(val) == mod:
        progress += 1
    if progress > 12:
        progress = 12
    elif progress < 0:
        progress = 0
    bingo.old_progress = bingo.progress
    bingo.progress = progress
    if bingo.old_progress < progress:
        flag = True
    return bingo, flag
