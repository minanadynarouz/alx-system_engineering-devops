#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - loop runs infinitly
 * Return: zero if broken
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
 * main - program that creates 5 zombies processes
 * Return: 0 if success, 1 otherwise
 */

int main(void)
{
	pid_t childs_pid;
	int counter = 0;

	while (counter < 5)
	{
		if (childs_pid > 0)
		{
			childs_pid = fork();
			printf("Zombie process created, PID: %d\n", childs_pid);
			sleep(1);
			counter++;
		}
		else
		{
			return(1);
		}
	}
	infinite_while();
	return (0);
}
