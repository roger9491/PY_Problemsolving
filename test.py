
'''
MC  AT  #Cust   DT1 BR1 OP1 Serverst    #Cust   DT2 BR2 OP2 Serverst
50  70  1       70  50  100 down                    90      idle
70  110 1               100 down        1       100 90      busy
90  110 1               100 dwon        1       250     240 down
100 110 1       120         busy        1       250     240 down
110 130 2       10  300     busy        1       250     240 down







Events and associated clocks:
Arrival of a customer to queue 1 (clock AT)
    Arrival to queue 1 (new value for AT clock): This event is always scheduled each time an arrival occurs.
Service completion at server 1 (new value for DT1 clock): This event will be triggered if the new arrival finds the server idle.

Service completion at server 1 (clock DT1)
Service completion at server 1(new value for DT1 clock): This event will occur if there is one or more customers in queue 1.
Service completion at server 2 (new value for DT2 clock): This event will occur if the customer who just completed its service at server 1 finds server 2 idle.
The occurrence of a service completion event at server 1 may cause server 1 to get blocked, if queue 2 is full.

Service completion at server 2 (clock DT2)
Service completion at server 2 (new value for D21 clock): This event will occur if there is one or more customers in queue 2.
Service completion at server 1 (new value for DT1 clock): This event will occur if server 1 was blocked.

Server 1 breaks down (clock BR1)
Server 1 becomes operational (new value for OP1 clock): This event gives the time in the future when the server will be repaired and will become operational. If the server was busy when it broke down, update the clock of the service completion event at server 1 to reflect the delay due to the repair.

Server 1 becomes operational (clock OP1)
Server 1 breaks down (new value for BR1 clock): This event gives the time in the future when the server will break down. During this time the server is operational.
Service completion time (new value for DT1): If the server was idle when it broke down, and queue 1 is not empty at the moment it becomes operational, then a new service will begin

Server 2 breaks down (clock BR2)
Server 2 becomes operational (new value for OP2 clock): This event gives the time in the future when server 2 will be repaired, and therefore it will become operational. During that time the server is broken down.
If server 2 was busy when it broke down, update the clock of the service completion event at server 2 to reflect the delay due to the repair.

Server 2 becomes operational (clock OP2)
Server 2 breaks down (new value for BR2 clock): This event gives the time in the future when server 2 will break down. During this time the server is operational.
Service completion time (new value for DT2): If the server was idle when it broke down, and queue 2 is not empty at the moment it becomes operational, then a new service will begin.










'''

