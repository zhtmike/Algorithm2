/* Naive implementation of the union-find data structure */

#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

typedef struct Union_Finder {
    int name;
    unsigned int size;
    struct Union_Finder *leader;
} union_finder;

union_finder *nodes[100];
int counter = 0;

int find(int name) {
    /* Return the name of the group */
    return nodes[name]->leader->name;
}

void merge(int name1, int name2) {
    /* Merge the unions containing node1 and node2 ,
     * And left the remain nodes unchanged.
     */

    // Check which union is bigger
    union_finder *small_union, *large_union;
    if (nodes[name1]->leader->size >= nodes[name2]->leader->size) {
        large_union = nodes[name1]->leader;
        small_union = nodes[name2]->leader;
    } else {
        large_union = nodes[name2]->leader;
        small_union = nodes[name1]->leader;
    }

    // Assign nodes in small union to the large union
    large_union->size += small_union->size;
    for (int i = 0; i < counter; ++i) {
        if (nodes[i]->leader == small_union)
            nodes[i]->leader = large_union;
    }
}

void insert() {
    /* Insert Node and assign it to be its own Union */
    nodes[counter] = malloc(sizeof(union_finder));
    nodes[counter]->size = 1;
    nodes[counter]->name = counter;
    nodes[counter]->leader = nodes[counter];
    counter++;
}

void clear() {
    for (int i = 0; i < counter; ++i) {
        free(nodes[i]);
    }
    counter = 0;
}

static PyObject *unionFinder_find(PyObject *self, PyObject *args) {
    /* Wrapper of find.
     * arg: name
     */
    int name;
    PyArg_ParseTuple(args, "i", &name);
    if (name>=counter)
        return PyExc_IndexError;
    return Py_BuildValue("i", find(name));
}

static PyObject *unionFinder_insert(PyObject *self, PyObject *args) {
    /* Wrapper of insert.
     * arg: total number
     */
    int num;
    PyArg_ParseTuple(args, "i", &num);
    for (int i = 0; i < num; ++i) {
        insert();
    }
    return Py_BuildValue("");
}

static PyObject *unionFinder_merge(PyObject *self, PyObject *args) {
    /* Wrapper of merge
     * arg: name 1, name 2
     */
    int a, b;
    PyArg_ParseTuple(args, "ii", &a, &b);
    merge(a, b);
    return Py_BuildValue("");
}

static PyObject *unionFinder_clear(PyObject *self, PyObject *args) {
    /* Wrapper of merge
     * arg: name 1, name 2
     */
    clear();
    return Py_BuildValue("");
}

static char unionFinder_docs[] =
        "find(): find the leader of the node\ninsert(): insert n nodes\nmerge(): merge the union\nclear(): clear the nodes\n";

static PyMethodDef unionFinder_funcs[] = {
        {"insert", (PyCFunction) unionFinder_insert, METH_VARARGS, unionFinder_docs},
        {"find",   (PyCFunction) unionFinder_find,   METH_VARARGS, unionFinder_docs},
        {"merge",  (PyCFunction) unionFinder_merge,  METH_VARARGS, unionFinder_docs},
        {"clear",  (PyCFunction) unionFinder_clear,  METH_VARARGS, unionFinder_docs},
        {NULL, NULL, 0, NULL}
};

static struct PyModuleDef unionFinder = {
        PyModuleDef_HEAD_INIT,
        "unionFinder",
        "",
        -1,
        unionFinder_funcs
};

PyMODINIT_FUNC PyInit_unionFinder(void) {
    return PyModule_Create(&unionFinder);
}