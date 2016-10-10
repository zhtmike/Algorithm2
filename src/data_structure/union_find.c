/* Naive implementation of the union-find data structure */

#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

typedef struct Union_Finder {
    int name;
    unsigned int size;
    struct Union_Finder *leader;
} union_finder;

int find(union_finder *node) {
    /* Return the name of the group */
    return node->leader->name;
}

void merge(union_finder *node1, union_finder *node2, union_finder *nodes[], int size) {
    /* Merge the unions containing node1 and node2 ,
    And left the remain nodes unchanged. */

    // Check which union is bigger
    union_finder *small_union, *large_union;
    if (node1->leader->size >= node2->leader->size) {
        large_union = node1->leader;
        small_union = node2->leader;
    } else {
        large_union = node2->leader;
        small_union = node1->leader;
    }

    // Assign nodes in small union to the large union
    large_union->size += small_union->size;
    for (int i = 0; i < size; ++i) {
        if (nodes[i]->leader == small_union)
            nodes[i]->leader = large_union;
    }
}

void initialize(union_finder *nodes[], int size, int names[]) {
    /* Initiate all the nodes to be in its own union */
    for (int i = 0; i < size; ++i) {
        nodes[i] = malloc(sizeof(union_finder));
        nodes[i]->size = 1;
        nodes[i]->name = names[i];
        nodes[i]->leader = nodes[i];
    }
}

int main() {
    const int NUM = 4;
    union_finder *u[NUM];
    int names[4] = {0, 1, 2, 3};
    initialize(u, NUM, names);

    merge(u[1], u[2], u, NUM);
    merge(u[2], u[3], u, NUM);

    for (int i = 0; i < NUM; ++i) {
        printf("%i\n", find(u[i]));
    }

    return 0;
}