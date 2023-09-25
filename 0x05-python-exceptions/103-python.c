#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints Python byte objects
 * @p: pointer to a python object
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	int index;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %.*s\n", (int)size, str);

	printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
	for (index = 0; index < size && index < 10; index++)
		printf(" %02hhx", str[index]);
	printf("\n");
}

/**
 * print_python_float - Prints Python float objects
 * @p: pointer to a python object
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %0.16g\n", value);
}

/**
 * print_python_list - Prints Python list objects
 * @p: pointer to a python object
 */
void print_python_list(PyObject *p)
{
	long int size;
	long int alloc;
	int index;
	PyObject *item;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (index = 0; index < size; index++)
	{
		item = PyList_GetItem(p, index);
		printf("Element %d: %s\n", index, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}
