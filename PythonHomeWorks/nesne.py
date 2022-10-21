class CountFromBY:
    #method
    def increase(self)->None:
        self.val += self.incr

    def __init__(self, v:int=0, i:int=1) -> None:
        self.val  = v
        self.incr = i

    def __repr__(self)->str:
        return str(self.val)

a = CountFromBY(10,2)

a.increase()
# CountFromBy.increase(a)

b = CountFromBY()

print(a.val, a.incr)
a.increase()
print(a.val, a.incr)
print(a)

c = CountFromBY()

print(c.val, c.incr)

c.increase()
print(c)