#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 0 in case of no cycle and 1 at the opposite
 */

int check_cycle(listint_t *list)
{
	listint_t *p2;
	listint_t *prev;

	p2 = list;
	prev = list;
	while (p2 && p2->next)
	{
		p2 = p2->next->next;
		prev = prev->next->next;

		if (prev == p2)
		{
			return (1);
		}
	}
	return (0);
}
