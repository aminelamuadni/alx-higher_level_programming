#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about Python bytes objects.
 * @p: Pointer to a Python object.
 */
void print_python_bytes(PyObject *p)
{
	long int size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size > 9)
		size = 10;
	else
		size++;

	printf("  first %ld bytes:", size);
	for (i = 0; i < size; i++)
		printf(" %02hhx", str[i]);
	printf("\n");
}

/**
 * print_python_list - Print information about Python list objects.
 * @p: Pointer to a Python object.
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyObject *item;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
