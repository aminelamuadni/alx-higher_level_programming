#include "lists.h"
#include <stdio.h>

/**
 * reverse - Reverses a linked list from a given node.
 * @head: A pointer to the node to start the reverse from.
 * Return: Pointer to the first node of the reversed list.
 */
listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 * Return: 0 if not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half, *prev_slow = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast)
		slow = slow->next;

	second_half = reverse(slow);
	prev_slow->next = NULL;

	while (*head && second_half)
	{
		if ((*head)->n != second_half->n)
		{
			reverse(second_half);
			return (0);
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}

	if (!(*head) && !second_half)
		return (1);

	return (0);
}
