#include <Python.h>

/**
 * print_python_string - Print information about Python string objects.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int len;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	len = PyUnicode_GET_LENGTH(p);
	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("  type: compact ascii\n");
		printf("  length: %ld\n", len);
		printf("  value: %s\n", PyUnicode_AsUTF8AndSize(p, &len));
	}
	else if (PyUnicode_IS_COMPACT(p))
	{
		printf("  type: compact unicode object\n");
		printf("  length: %ld\n", len);
		printf("  value: %s\n", PyUnicode_AsUTF8AndSize(p, &len));
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}
