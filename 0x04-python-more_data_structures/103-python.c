#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints details about a Python bytes object.
 * @p: The Python bytes object.
 *
 * Return: Void.
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, i, limit;

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

	limit = (size > 9) ? 10 : size + 1;

	printf("  first %ld bytes:", limit);
	for (i = 0; i < limit; i++)
	{
		printf(" %02hhx", str[i]);
	}
	printf("\n");
}

/**
 * print_python_list - Prints details about a Python list, and any bytes
 *				   objects within it.
 * @p: The Python list object.
 *
 * Return: Void.
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
