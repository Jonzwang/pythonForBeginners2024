

def with_while_loop():
    f0 = 0
    f1 = 1

    count = 0
    limit = 10

    print(f"0: {f0}")

    while count < limit:
        print(f"{count+1}: {f1}")
        f2 = f0 +f1
        f0 = f1
        f1 = f2
        count += 1

with_while_loop()