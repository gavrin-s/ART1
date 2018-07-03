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
    pass


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


def main():
    perform_art1()
    display_customer_database()
    for customer in range(MAX_CUSTOMERS):
        make_recommendation(customer)