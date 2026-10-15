N = ord("M") % 3 + 1

print(f"Мій варіант завдання: {N} \n\n")


def savecache(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache:
            print(f"[{func.__name__}] результат з кешу для {args}, {kwargs}")
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        print(f"[{func.__name__}] обчислено і додано в кеш для {args}, {kwargs}")
        return result

    return wrapper


@savecache
def add(a, b):
    return a + b


@savecache
def power(base, exp=2):
    return base ** exp


@savecache
def concat_strings(*words, sep=" "):
    return sep.join(words)


if __name__ == "__main__":
    print(add(2, 3))
    print(add(2, 3))
    print(add(5, 7))

    print(power(2))
    print(power(2))
    print(power(2, exp=3))

    print(concat_strings("Python", "lang"))
    print(concat_strings("Python", "lang"))
    print(concat_strings("Python", "lang", sep="-"))


