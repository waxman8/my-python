import sys
import math

w, h = [int(i) for i in input().split()]
n = int(input())
jx, jy = [int(i) for i in input().split()]
print(f"w{w} h{h} and start at {jx} {jy}", file=sys.stderr, flush=True)

ox=0
oy=0
mx=w-1
my=h-1

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    print(f"go: {bomb_dir} {jx} {jy}", file=sys.stderr, flush=True)

    if 'D' in bomb_dir:
        oy=jy
        jy = oy + math.ceil((my - oy) / 2)  
    if 'U' in bomb_dir:
        my=jy
        jy = my - math.ceil((my - oy) / 2)  
    if 'L' in bomb_dir:
        mx=jx
        jx = mx - math.ceil((mx - ox) / 2)  
    if 'R' in bomb_dir:
        ox=jx
        jx = ox + math.ceil((mx - ox) / 2)  
 
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # the location of the next window Batman should jump to.
    print(f'{jx} {jy}')
