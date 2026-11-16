P1, nP1, vP1 = input().split(maxsplit=3)
P2, nP2, vP2 = input().split(maxsplit=3)

print(f"VALOR A PAGAR: R$ {((int(nP1) * float(vP1)) + (int(nP2) * float(vP2))):.2f}")