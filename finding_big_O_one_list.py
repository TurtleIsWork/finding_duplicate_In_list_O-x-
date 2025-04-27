import time
import random
from multiprocessing.reduction import duplicate

s = set()

def make_a_list_n(size):
    duplicate_number = random.randint(1,size)
    number_list = []
    for number in range(size):
        number_list.append(number)
    number_list.append(duplicate_number)
    random.shuffle(number_list)
    return number_list

def find_duplicet_using_in(list):
    number_set = set()
    for a in list:
        if a in number_set:
            return a
        number_set.add(a)
    return list[-1]

def find_duplicet_using_math(list):
    total = 0
    for ni in range(len(list) - 1):
        total += ni+1

    return sum(list)-total


def how_long(function, list_a):
    start = time.perf_counter()
    function(list_a)
    end = time.perf_counter()
    return end - start



if __name__ == "__main__":
    print("-------------------------------------------------------")
    tests = 1000000
    total_in_time = 0.
    total_math_time = 0.
    total_in_time_two = 0.
    total_math_time_two = 0.
    for i in range(tests):

        list = make_a_list_n(50)
        total_in_time += how_long(find_duplicet_using_in, list)
        total_math_time += how_long(find_duplicet_using_in, list)

    for i in range(tests):

        list = make_a_list_n(100)
        total_in_time_two += how_long(find_duplicet_using_in, list)

        total_math_time_two += how_long(find_duplicet_using_in, list)

    print(f"sample size of {tests}")
    print(f"in took an average of {total_in_time / tests} and a total of {total_in_time * 1000:.3f} ms for n size of {50}\n"
          f"math took an average of {total_math_time / tests} and a total of {total_math_time * 1000:.3f} ms for n size of {50}")
    print(f"in took an average of {total_in_time_two / tests} and a total of {total_in_time_two * 1000:.3f} ms for n size of {100}\n"
          f"math took an average of {total_math_time_two / tests} and a total of {total_math_time_two * 1000:.3f} ms for n size of {100}")
