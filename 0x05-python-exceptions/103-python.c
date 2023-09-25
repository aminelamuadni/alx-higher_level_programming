#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints Python byte objects
 * @p: pointer to a python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	int index;
	char *str;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));

	printf("  trying string: %s\n", str);

	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	for (index = 0; index < size + 1 && index < 10; index++)
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
	char *str;

	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_list - Prints Python list objects
 * @p: pointer to a python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	int index;
	PyObject *item;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (!PyList_CheckExact(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (index = 0; index < size; index++)
	{
		item = PyList_GET_ITEM(p, index);
		printf("Element %d: %s\n", index, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}
