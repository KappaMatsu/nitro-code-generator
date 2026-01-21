#██╗  ██╗ █████╗ ██████╗ ██████╗ █████╗ ███╗    ███╗ █████╗ ████████╗███████╗██╗   ██╗
#██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝██╔════╝██║   ██║
#█#████╔╝ ███████║██████╔╝██████╔╝███████║██╔████╔██║███████║   ██║   ███████╗██║   ██║
#██#╔═██╗ ██╔══██║██╔═══╝ ██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══██║   ██║   ╚════██║██║   ██║
#██║  ██╗██║  ██║██║     ██║     ██║  ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████║╚██████╔╝
#╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ 
#
 #       PRIVATE SOURCE CODE — DO NOT COPY
#
 #       This code belongs to: KappaMatsu  
  #      Unauthorized copying, modification,  
   #     or redistribution is strictly forbidden.
#
 #       © 2026 KappaMatsu. All rights reserved.

import random
import string
import os

alphabet = string.ascii_letters + string.digits
length = 16
prefix = "https://discord.gift/"
output_file = "nitro_codes.txt"

count = int(input("Combien de combinaisons voulez-vous générer ? "))
def generate_combinaison(length):
    return ''.join(random.choice(alphabet) for _ in range(length))

block_size = 1000000000
generated_total = 0

if os.path.exists(output_file):
    os.remove(output_file)

with open(output_file, 'a', encoding='utf-8') as f:
    while generated_total < count:
        current_block_size = min(block_size, count - generated_total)
        for _ in range(current_block_size):
            combinaison = generate_combinaison(length)
            f.write(prefix + combinaison + '\n')
        generated_total += current_block_size
        print(f"{generated_total} combinaisons générées...")
