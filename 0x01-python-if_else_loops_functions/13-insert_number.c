#include "lists.h"
/**
 * insert_node - function in C that inserts a number into a sorted
 * singly linked list.
 * @head: pointer to head of list
 * @number: integrer
 * Return: number of nodes
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, *new = NULL;

	tmp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (!*head)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	if (number < 0)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (tmp)
	{
		if (tmp->next == NULL)
		{
			new->next = NULL;
			tmp->next = new;
			return (new);
		}
		if (tmp->n < number && number <= tmp->next->n)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	return (NULL);
}
