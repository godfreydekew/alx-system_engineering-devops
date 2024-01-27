#include <stdio.h>
#include <wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

/**
 *infinite_while - A function which creates a infinite loop
 * Return: Zero on success
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 *main - Creates five zombie process
 *Return: Zero on success
 */

int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		if (!fork())
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}

	}

	infinite_while();
}
