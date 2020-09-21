from argparse import ArgumentParser
import heap


def test_heapify():
    print("#test_heapify")
    A = [1]
    heap.heapify(A, 0)
    print("Heapify length 1:", A == [1])

    A = [2, 1]
    heap.heapify(A, 0)
    print("Heapify two out of order:", A == [1, 2])

    A = [1, 2]
    heap.heapify(A, 0)
    print("Heapify two in order:", A == [1, 2])

    A = [5, 4, 3, 2, 1]
    print("A: ",A)
    heap.heapify(A, 1)
    print("Heapify 1:", A == [5, 1, 3, 2, 4])

    A = [5, 1, 3, 2, 4]
    heap.heapify(A, 0)
    print("Heapify 0:", A == [1, 2, 3, 5, 4])


def is_min_heap(A):
    def parent(i):
        return (i - 1) // 2
    return all(A[parent(x)] <= A[x] for x in range(1, len(A)))


def shuffled_list(length, seed):
    A = list(range(10, length + 10))
    import random
    r = random.Random(seed) # pseudo random, so it is repeatable
    r.shuffle(A)
    return A


def test_build_heap():
    print("#test_build_heap")
    for x in range(5, 41, 5):
        A = shuffled_list(x, x)
        heap.buildHeap(A)
        print("buildHeap(shuffled_list({}, {})) is a min heap: ".format(x, x), is_min_heap(A))


def test_insert_extract():
    print("#test_insert_extract")
    for round in range(2):
        order = shuffled_list(30, round)
        A = []
        for x in range(10):
            heap.heapInsert(A, order.pop())
            heap.heapInsert(A, order.pop())
            has_heap_property = is_min_heap(A)
            min_elem = min(A)
            extracted = heap.heapExtractMin(A)
            print("Correctly extracted min: {}, maintained heap property: {}".format(
                min_elem == extracted, has_heap_property and is_min_heap(A)))


def is_sorted(A):
    for i in range(0, len(A)- 1):
        if not A[i] >= A[i+1]:
            return False
    return True



def within_30_percent(expected, actual):
    margin = 0.3 * expected
    low = expected - margin
    hi = expected + margin
    return low <= actual <= hi

    
def report_counts_on_basic_ops(A, expected_build_count, expected_extract_count, expected_insert_count):
    print("Counts for list of len: {}".format(len(A)))
    heap.reset_counts()
    heap.buildHeap(A)
    bh = heap.current_counts()['heapify_call_count']
    print("buildHeap heapify calls within 30% of expected number of calls: {}".format(within_30_percent(expected_build_count, bh)))

    heap.reset_counts()
    m = heap.heapExtractMin(A)
    ex = heap.current_counts()['heapify_call_count']
    print("heapExtractMin heapify calls within 30% of expected number of calls: {}".format(within_30_percent(expected_extract_count, ex)))

    heap.reset_counts()
    heap.heapInsert(A, m)
    ins = heap.current_counts()['swap_count']
    print("heapInsert swap calls within 30% of expected number of calls: {}".format(within_30_percent(expected_insert_count, ins)))


def test_counts():
    print("#test_counts:")
    
    A = shuffled_list(400, 0)
    report_counts_on_basic_ops(A, 487, 8, 8)
    
    A = shuffled_list(10000, 0)
    report_counts_on_basic_ops(A, 12420, 14, 13)

    A = shuffled_list(100000, 0)
    report_counts_on_basic_ops(A, 124571, 17, 16)

            
def test_all():
    test_heapify()
    test_build_heap()
    test_insert_extract()
    test_counts()


def test_by_number(test_number):
    if test_number == 1:
        test_heapify()
    elif test_number == 2:
        test_build_heap()
    elif test_number == 3:
        test_insert_extract()
    else:
        test_counts()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--test", dest="test_number",
                        type=int, help="The number of the test to run [1-4]")
    args = parser.parse_args()

    if args.test_number:
        test_by_number(args.test_number)
    else:
        test_all()
