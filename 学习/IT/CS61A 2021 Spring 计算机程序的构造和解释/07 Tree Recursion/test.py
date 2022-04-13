# def move_tower(n, start_peg, end_peg):
#     if n == 1:
#         move_disk(start_peg, end_peg)
#     else:
#         spare_peg = 6- start_peg - end_peg
#         move_tower(n - 1, start_peg, spare_peg)
#         move_disk(start_peg, end_peg)
#         move_tower(n - 1, spare_peg, end_peg)
        

def move_tower(n, start_peg, end_peg):
    if n == 1:
        return 1
    else:
        spare_peg = 6- start_peg - end_peg # 1, 2, 3 => 
        return move_tower(n - 1, start_peg, spare_peg) + \
        1 + \
        move_tower(n - 1, spare_peg, end_peg)

print(move_tower(4, 1, 3))