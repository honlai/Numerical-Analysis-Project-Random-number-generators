import G1 as g1
import G2 as g2


if __name__=="__main__": 
    Nmax=10
    print(f"\nPRNGs give {Nmax} random numbers")
    print("\nG1:")
    L_g1 = g1.RNG(10)
    k=0
    for rnd in L_g1:
        print(f'{k}: {rnd}')
        k+=1

    print("\nG2:")
    sd = g2.get_seed()
    custom_rng = g2.CustomPRNG2(seed=sd)
    for k in range(10):
        print(f'{k}: {custom_rng.random()}')
        