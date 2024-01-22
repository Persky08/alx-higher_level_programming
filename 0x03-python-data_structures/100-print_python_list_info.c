#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - a function that prints python info
 * @p: python list
 *
 * Return: python info
 */

void print_python_list_info(PyObject *p)
{
	int i;
	Py_ssize_t size, allocated;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
