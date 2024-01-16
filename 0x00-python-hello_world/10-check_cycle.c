#include "lists.h"
/**
 * check_cycle- a function to check if a list has a cycle
 * @list: singly linked list
 *
 * Return: 1 if it has a cylce
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_pointer;
	listint_t *fast_pointer;

	slow_pointer = list;
	fast_pointer = list;

	if (list == NULL)
	{
		return (0);
	}
	while (fast_pointer != NULL && fast_pointer->next != NULL)
	{
		slow_pointer = slow_pointer->next;
		fast_pointer = fast_pointer->next->next;

		if (slow_pointer == fast_pointer)
		{
			return (1);
		}
	}
	return (0);
}
