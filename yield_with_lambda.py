'''Note that the expensive checks only happen at the start of each loop, rather than all at once.'''
def expensive_check1():
    print("expensive_check1")
    return True


def expensive_check2():
    print("expensive_check2")
    return True


def expensive_check3():
    print("expensive_check3")
    return True


def do_the_thing(*args):
    print(args)


if __name__=="__main__":
    for check, args in (lambda: (
                                (yield (expensive_check1(), ["foo", "bar"])),
                                (yield (expensive_check2(), ["baz"])),
                                (yield (expensive_check3(), [])),
                        ))():
        if check:
            do_the_thing(*args)
            continue
        raise Exception("oh noes!!!")
    else:
        print("all OK!")