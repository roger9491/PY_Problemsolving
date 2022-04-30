#include <stdio.h>
#include "sim.h"
int main()
{
    struct node *head = NULL;
    head = createNode(3, 0.200000);
    head->next = createNode(2, 0.250000);
    head->next->next = createNode(1, 0.600000);
    int a = 3;
    printLists(head);
    printf("請選擇1:插入事件2:找到下一個事件並移除0:結束\n");
    scanf("%d", &a);
    while (a != 0)
    {
        if (a == 1)
        {
            int c = 0;
            double d = 0.0;
            printf("type:");
            scanf("%d", &c);
            printf("clock:");
            scanf("%lf", &d);
            head = insertNode(head, createNode(c, d));
            printf("(FEL)");
            printLists(head);
            printf("請選擇1:插入事件2:找到下一個事件並移除0:結束\n");
            scanf("%d", &a);
        }
        else if (a == 2)
        {
            int t1;
            double t2;
            t1 = head->type;
            t2 = head->clock;
            head = head->next;
            printf("(FEL)");
            printLists(head);
            printf("(Current Event)type: %d clock:%2f --> \n", t1, t2);
            printf("請選擇1:插入事件2:找到下一個事件並移除0:結束\n");
            scanf("%d", &a);
        }
    }
}
