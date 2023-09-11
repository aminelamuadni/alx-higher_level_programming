#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of the linked list.
 * Return: 0 if not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev_slow = *head, *second_half = NULL;
	int i;
	int size = 0;
	listint_t *tmp;
	int* stack;

	if (!*head)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
		size++;
	}
	size *= 2;

	if (fast)
	{
		slow = slow->next;
		size++;
	}

	second_half = slow;
	prev_slow->next = NULL;

	stack = (int*)malloc((size/2) * sizeof(int));
	if (!stack) {
		return (0);
	}

	tmp = *head;
	for (i = 0; i < size/2; i++)
	{
		stack[i] = tmp->n;
		tmp = tmp->next;
	}

	while (second_half && i > 0)
	{
		if (stack[--i] != second_half->n)
			return (0);
		second_half = second_half->next;
	}

	free(stack);

	return (1);
}
