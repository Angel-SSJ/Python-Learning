from collections import deque

'''Este modulo proporciona estructuras de datos avanzadas mas eficientes
deque(Double-Ended queue)
    Es mas rapido que una lista para inserciones y eliminaciones en los extremos
    soporta operaciones de cola y pila de forma optima
'''


dq = deque([1,2,3])
dq.append(4)
dq.appendleft(0)
print(dq)

dq.pop()
dq.popleft()
print(dq)
