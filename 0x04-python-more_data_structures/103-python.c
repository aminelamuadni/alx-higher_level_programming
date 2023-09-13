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

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

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
	PyListObject *list;
	PyObject *item;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
