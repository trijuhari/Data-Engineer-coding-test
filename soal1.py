def reversed_string(string):
    # function for reversed string

    return (''.join(reversed(string)))


def displayMulti(string, repeat_string):
    # check if len string  more than 3  get  three first letter and repeat N times (repeat_string)

    if len(string) >= 3:
        string_name = string[0:3]
        repeat = string_name * repeat_string
    else:
        string_name = reversed_string(string)
        repeat = string_name * repeat_string

    return repeat


def soal_1():
    print("===== Soal nomor 1 =====")
    print(displayMulti("Jakarta", 2))
    print(displayMulti("Jakarta", 3))
    print(displayMulti("BBM", 2))
    print(displayMulti("Or", 3))




def main():
    soal_1()


if __name__ == '__main__':
    main()

