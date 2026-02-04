def tree(n):
    if n <= 0:
        return [], "empty"

    width = 2 * n - 1
    tree = []
    for i in range(1, n + 1):
        stars = 2 * i - 1
        pad = (width - stars) // 2
        tree.append('_' * pad + '#' * stars + '_' * pad)

    trunk = '_' * ((width - 1) // 2) + '#' + '_' * ((width - 1) // 2)
    tree.append(trunk)
    tree.append(trunk)
    print(tree)


tree(5)