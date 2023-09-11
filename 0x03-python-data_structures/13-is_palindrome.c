#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * list_size - Calculates the size of a linked list.
 * @head: Pointer to the head of the linked list.
 * Return: Size of the list.
 */
int list_size(listint_t *head)
{
	listint_t *fast = head, *slow = head;
	int size = 0;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		size++;
	}

	size *= 2;
	if (fast)
		return (size + 1);
	return (size);
}

/**
 * fill_stack - Fills a stack from a linked list.
 * @head: Pointer to the head of the linked list.
 * @stack: Pointer to the stack.
 * @size: Size of the list.
 */
void fill_stack(listint_t *head, int *stack, int size)
{
	int i;
	listint_t *tmp = head;

	for (i = 0; i < size / 2; i++, tmp = tmp->next)
		stack[i] = tmp->n;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of the linked list.
 * Return: 0 if not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *second_half = NULL;
	int size;
	int *stack;

	if (!*head)
		return (1);

	size = list_size(*head);
	stack = (int *)malloc((size / 2) * sizeof(int));

	if (!stack)
		return (0);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast)
		slow = slow->next;
	if (prev)
		prev->next = NULL;

	second_half = slow;
	fill_stack(*head, stack, size);

	while (second_half && size > 0)
	{
		if (stack[--size] != second_half->n)
		{
			free(stack);
			return (0);
		}
		second_half = second_half->next;
	}

	free(stack);
	return (1);
}
