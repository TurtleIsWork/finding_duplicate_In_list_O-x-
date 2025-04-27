import time
import random
from multiprocessing.reduction import duplicate

s = set()

def make_two_lists_with_a_duplicet(size):
    duplicate_number = random.randint(-2**31-1,2**31-1)
    list_a = []
    list_b = []
    adding = random.randint(-2**31-1,2**31-1)
    for _ in range(size-1):
        while adding in list_b or adding == duplicate_number:
            adding = random.randint(-2**31-1,2**31-1)
        list_a.append(adding)
        while adding in list_a or adding == duplicate_number:
            adding = random.randint(-2**31-1,2**31-1)
        list_b.append(adding)

    list_a.insert(random.randint(0,size-2),duplicate_number)
    list_b.insert(random.randint(0,size-2),duplicate_number)

    return list_a,list_b

def find_duplicet_using_in(list_a, list_b):
    number_set = set()
    for an, bn in zip(list_a, list_b):
        number_set.add(an)
        if bn in number_set:
            return bn

def find_duplicet_using_len(list_a, list_b):
    big_list = list_a + list_b
    number_set = set()
    set_len = int
    for i in big_list:
        set_len = number_set.__len__()
        number_set.add(i)
        if set_len == number_set.__len__():
            return i

def how_long(function, list_a, list_b):
    start = time.perf_counter()
    function(list_a, list_b)
    end = time.perf_counter()
    return end - start


# def main():
#     tests = 10
#     total_in_time = 0.
#     total_len_time = 0.
#     lists = make_two_lists_with_a_duplicet(50)
#
#     for i in range(tests):
#         total_in_time = how_long(find_duplicet_using_in(lists[0],lists[1]))
#         total_len_time = how_long(find_duplicet_using_len(lists[0],lists[1]))
#
#     print(f"in took an avrege of {total_in_time/tests} and a total of {total_in_time}\n"
#           f"len took an avrege of {total_len_time/tests} and a total of {total_len_time}")


if __name__ == "__main__":
    print("-------------------------------------------------------")
    tests = 10000
    total_in_time = 0.
    total_len_time = 0.
    total_in_time_two = 0.
    total_len_time_two = 0.
    for i in range(tests):

        lists = make_two_lists_with_a_duplicet(50)

        total_in_time += how_long(find_duplicet_using_in, lists[0], lists[1])
        total_len_time += how_long(find_duplicet_using_len, lists[0], lists[1])

    for i in range(tests):

        lists = make_two_lists_with_a_duplicet(100)

        total_in_time_two += how_long(find_duplicet_using_in, lists[0], lists[1])
        total_len_time_two += how_long(find_duplicet_using_len, lists[0], lists[1])

    print(f"sample size of {tests}")
    print(f"in took an avrege of {total_in_time / tests} and a total of {total_in_time * 1000:.3f} ms for n size of {50}\n"
          f"len took an avrege of {total_len_time / tests} and a total of {total_len_time * 1000:.3f} ms for n size of {50}")
    print(f"in took an avrege of {total_in_time_two / tests} and a total of {total_in_time_two * 1000:.3f} ms for n size of {100}\n"
          f"len took an avrege of {total_len_time_two / tests} and a total of {total_len_time_two * 1000:.3f} ms for n size of {100}")
