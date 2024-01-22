#include "lists.h"
/**
 * insert_node - a function that inserts node
 * @head: pointer to the head of the node
 * @number: the position to insert
 *
 * Return: new node
 */


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current, *old;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	current = *head;
	old = NULL;

	while (current != NULL && current->n < number)
	{
		old = current;
		current = current->next;
	}
	if (old == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		new->next = old->next;
		old->next = new;
	}
	return (new);
}
