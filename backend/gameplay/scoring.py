import backend.gameplay.contants as C


def big_four_winds(tileset, pair) -> tuple[bool, int]:
    for tiles in tileset:
        if not len(tiles) >= 3 and tiles not in C.WINDS:
            return (False, 0)
    return (True, 88) if pair.is_valid() else False

def big_three_dragons(tileset, pair) -> tuple[bool, int]:
    for tiles in tileset:
        if not len(tiles) >= 3 and tiles not in C.DRAGONS:
            return False
    return (True, 88) if pair.is_valid() else False
    
def all_green(tileset, pairs) -> tuple[bool, int]:
    GREEN_TILES = [C.BAM_2, C.BAM_3, C.BAM_4, C.BAM_6, C.BAM_8, C.GREEN_DRAGON]
    for tiles in tileset:
        if tiles in GREEN_TILES: 
            continue
        else: 
            return (False, 0)
    for pair in pairs:
        if pair in GREEN_TILES: 
            continue
        else: 
            return (False, 0)
    return (True, 88)

def nine_gates(tileset):
    WAN_GATES = [
        (C.WAN_1, 3),
        (C.WAN_2, 1),
        (C.WAN_3, 1),
        (C.WAN_4, 1),
        (C.WAN_5, 1),
        (C.WAN_6, 1), 
        (C.WAN_7, 1), 
        (C.WAN_8, 1), 
        (C.WAN_9, 3)
    ]
    tiles = tileset.expand()



