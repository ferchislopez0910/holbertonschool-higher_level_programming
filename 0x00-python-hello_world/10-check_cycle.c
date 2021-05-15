#include "lists.h"
/**
 * check_cycle - prints all elements of a listint_t list
 * @list: pointer to head of list
 * Return: 1 if cycle or 0 is not.
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp_count = list, *tmp_2count = list;

	while (tmp_count && tmp_2count && tmp_2count->next)
	{
		tmp_2count = tmp_2count->next->next;
		tmp_count = tmp_count->next;
		if (tmp_count == tmp_2count)
			return (1);
	}
	return (0);
}
