#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_while - an infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
while (1)
{
sleep(2);
}
return (0);
}


/**
 * main - creates 5 zombie processes
 *
 * Return: 0
 */
int main(void)
{
int i = 0, pid = 0;

while (i++ < 5 && (pid = fork()) != 0)
{
printf("Zombie process created, PID: %d\n", pid);
if (i == 5)
infinite_while();
}
return (0);
}
