import numpy as np


MAX_ITEMS = 11
MAX_CUSTOMERS = 10
TOTAL_PROTOTYPE_VECTORS = 5

beta = 1.0
vigilance = 0.9

num_prototype_vectors = 0
prototype_vector = np.zeros(shape=(TOTAL_PROTOTYPE_VECTORS, MAX_ITEMS))

sum_vector = np.zeros(shape=(TOTAL_PROTOTYPE_VECTORS, MAX_ITEMS))

members = np.zeros(TOTAL_PROTOTYPE_VECTORS)

membership = np.ones(MAX_CUSTOMERS) * -1

item_names = ['Hammer', 'Paper', 'Snickers', 'Screwdriver', 'Pen',
              'Kit-Kat', 'Wrench', 'Pencil', 'Heath-Bar', 'Tape-Measure', 'Binder']

database = np.array([[0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                     [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                     [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
                     [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                     [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]])


def perform_art1():
    and_result = np.zeros(MAX_ITEMS)
    index = 0
    done = 0
    count = 50

    while not done:
        done = 1

        for index in range(MAX_CUSTOMERS):

            for pvec in range(TOTAL_PROTOTYPE_VECTORS):
                if members[pvec]:
                    and_result = vector_bitwise_and(database[index][0], prototype_vector[pvec][0])
                    mag_pe = vector_magnitude(and_result)
                    mag_p = vector_magnitude(prototype_vector[pvec][0])
                    mag_e = vector_magnitude(database[index][0])

                    result = mag_pe / (beta + mag_p)
                    test = mag_e / (beta + MAX_ITEMS)

                    if result > test:
                        if (mag_pe / mag_e) < vigilance:
                            if membership[index] != pvec:
                                old = membership[index]
                                membership[index] = pvec

                                if old >= 0:
                                    members[old] -= 1
                                    if members[old] == 0:
                                        num_prototype_vectors -= 1

                                members[pvec] += 1
                                if 0 <= old < TOTAL_PROTOTYPE_VECTORS:
                                    update_prototype_vector(old)
                                update_prototype_vector(pvec)
                                done = 0
                                break
                            else:
                                pass

            if membership[index] == -1:
                membership[index] = create_new_prototype_vector(database[index][0])
                done = 0

        count -= 1
        if not count:
            break
    return 0


def display_customer_database():
    pass


def make_recommendation(customer):
    pass


def vector_magnitude(vector):
    return np.sum(vector)


def vector_bitwise_and(v, w):
    return v & w


def create_new_prototype_vector(example):
    cluster = 0
    while members[cluster] and cluster < TOTAL_PROTOTYPE_VECTORS:
        cluster += 1

    if cluster == TOTAL_PROTOTYPE_VECTORS:
        return None

    print('Creating new cluster {}'.format(cluster))

    global num_prototype_vectors
    num_prototype_vectors += 1

    for i in range(MAX_ITEMS):
        prototype_vector[cluster][i] = example[i]
        print('{}'.format(example[i]))

    members[cluster] = 1
    print()

    return cluster


def update_prototype_vector(cluster):
    first = 1

    print('Recomputing prototype vector {} ({})'.format(cluster, members[cluster]))

    for item in range(MAX_ITEMS):
        prototype_vector[cluster][item] = 0
        sum_vector[cluster][item] = 0

    for customer in range(MAX_CUSTOMERS):
        if membership[customer] == cluster:
            if first:
                for item in range(MAX_ITEMS):
                    prototype_vector[cluster][item] = database[cluster][item]
                    sum_vector[cluster][item] = database[customer][item]
                first = 0
            else:
                for item in range(MAX_ITEMS):
                    prototype_vector[cluster][item] = prototype_vector[cluster][item] & database[customer][item]
                    sum_vector[cluster][item] += database[customer][item]


def main():
    perform_art1()
    display_customer_database()
    for customer in range(MAX_CUSTOMERS):
        make_recommendation(customer)