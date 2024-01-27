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
int main()
{
	int i;

	for (i = 0; i < 5; i++)
	{
		int pid = fork();

		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
		else
			exit(0);
	}

	infinite_while();

	return (0);
}
