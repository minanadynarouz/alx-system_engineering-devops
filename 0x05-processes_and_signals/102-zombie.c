#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Run an infinite while loop.
 * Return: 0
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
 * main - Create five zombies.
 * Return: 0
 */
int main(void)
{
	pid_t pid_child;
	char counter = 0;

	while (counter < 5)
	{
		pid_child = fork();
		if (pid_child > 0)
		{
			printf("Zombie process created, PID: %d\n", pid_child);
			sleep(1);
			counter++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (0);
}
