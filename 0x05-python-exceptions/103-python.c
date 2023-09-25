#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints basic info about Python bytes
 * @p: PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	char *content;
	int i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	content = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", content);
	printf("  first %ld bytes:", (size < 10 ? size + 1 : 10));
	for (i = 0; i < (size < 10 ? size + 1 : 10); i++)
		printf(" %02hhx", content[i]);
	printf("\n");
}

/**
 * print_python_float - prints basic info about Python floats
 * @p: PyObject float
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
	printf("  value: %lf\n", value);
}

/**
 * print_python_list - prints basic info about Python lists
 * @p: PyObject list
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

	size = ((PyVarObject *)p)->ob_size;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}
