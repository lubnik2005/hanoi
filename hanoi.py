class ring:
    value = 0
    def __init__(self,int_value):
        self.value = int_value
        self.visual = '='
        self.visual_len = len(self.visual)

    def __str__(self):
        return str(self.value)
    __repr__ = __str__
    
def power(base,exponent):
    if exponent == 0:
        return(1)
    value = 1
    for index in range(exponent):
        value = value * base
    return(value)

def recursive(pegs,initial,opposite,final,odd,moves):
    if moves == 0:
        return(pegs)
    if odd:
        pegs = move(pegs,initial,final)
    else: 
        initial, final = change_final(initial, final)
        pegs = move(pegs,initial,final)
        initial, final = change_final(initial, final)
    odd = not odd
    moves = moves - 1
    return(recursive(pegs,initial,opposite,final,odd,moves))

def size_to_diameter(size):
    return(size * 2) -1

def diameter_to_visual(diameter, visual_icon):
    return(diameter * visual_icon)

def generate_ring(size,m_size,visual_icon):
    current_ring_diameter   = size_to_diameter(size)
    max_ring_diameter       = size_to_diameter(m_size)  
    visual_string           = diameter_to_visual(current_ring_diameter, visual_icon) 
    visual_string           = visual_string.rjust(max_ring_diameter - (m_size - size))
    visual_string           = visual_string.ljust(max_ring_diameter)
    return(visual_string)

def generate_peg(lst,m_size):
    peg = []
    for ring in lst:
        visual_ring = generate_ring(ring.value,m_size,ring.visual)
        peg.append(visual_ring)
    for index in range(m_size - len(lst) + 1):
        peg_piece = generate_ring(1,m_size,'|')
        peg.append(peg_piece)
    return(peg)

def generate_pegs(pegs,m_size):
    visual_pegs = []
    for peg in pegs:
        visual_peg = generate_peg(peg,m_size)
        visual_pegs.append(visual_peg)
    return(visual_pegs)
    
def print_visual_pegs(pegs):
    reversed_pegs = []
    for peg in pegs:
        reversed_pegs.append(reversed(peg))

    for x, y, z in zip(*reversed_pegs):
        pass
        print(x, y, z) 

def moveVisual(pegs,m_size,init_peg, final_peg):
    moving = pegs[init_peg].pop()
    if (len(pegs[final_peg]) != 0) and (moving.value > pegs[final_peg][-1].value):
        print("Cannot complete action. Moving ring is begger than upper ring on peg")
    else:
        pegs[final_peg].append(moving)
    visual_pegs = generate_pegs(pegs,m_size)
    print_visual_pegs(visual_pegs)
    return(pegs)
    



def recursive(height,m_size,pegs,initPeg, finalPeg, oppositePeg):
    if height > 0:
        pegs = recursive(height-1,m_size,pegs,initPeg,oppositePeg,finalPeg)
        pegs = moveRing(pegs,m_size,initPeg,finalPeg)
        pegs = recursive(height-1,m_size, pegs, oppositePeg,finalPeg,initPeg)
    return(pegs)
def moveRing(pegs,m_size,initPeg,finalPeg):
    print("Moving Ring from",initPeg,"to",finalPeg)
    pegs = moveVisual(pegs,m_size, initPeg,finalPeg)
    return(pegs)

def user_input():
        # Creating number of rings 
    no_rings = True
    while no_rings:
        try:
            rings = int(input("How many rings?: "))
            if rings >=0:
                no_rings = False
        except Exception:
            pass
    return(rings)

def tower_of_hannoi(rings):
    ring_list = [ring(rings - int_value) for int_value in range(rings)]

    odd = not int(len(ring_list)) % 2 == 0
    expected_num_turns = power(2,rings) - 1
    print('Expected Number of turns:', expected_num_turns)
    pegs = [ [] for _ in range(3) ]
    pegs[0] = ring_list

# ===========================================================================
# <<It's not recursive>>, you said. <<Its a bit more complicated>>, you said
# ===========================================================================

    visual_pegs = generate_pegs(pegs,rings)
    print_visual_pegs(visual_pegs)
    recursive(rings,rings,pegs,0,2,1)

rings = user_input()
tower_of_hannoi(rings)
