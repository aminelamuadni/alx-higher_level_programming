#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (!list)
		return (0);

	tortoise = list;
	hare = list->next;

	while (tortoise != hare)
	{
		tortoise = tortoise->next;

		if (!hare || !hare->next)
			return (0);

		hare = hare->next->next;
	}

	return (1);
}
