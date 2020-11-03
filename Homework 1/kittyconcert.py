import cat
import numpy as np

def meow(iterations):
    for i in range(0, iterations):
        yield " ".join(["meow"] * 2**i)


if __name__ == "__main__":
    # task 1
    shark = cat.Cat("shark")
    tiger = cat.Cat("tiger")
    shark.greet(tiger)
    tiger.greet(shark)

    # task 2 - list comp
    print([i*i for i in range(0, 101) if (i*i) % 2 == 0])
    # task 3 - generators
    print([i for i in meow(10)])
    # task 4 - numpy
    arr = np.random.uniform(size=(5, 5))
    arr[arr*arr > 0.1] = 42
    print(arr)
    print(arr[:, 3])
