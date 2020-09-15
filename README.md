# localUDPthruput

run driver in terminal: 
  python driver.py <number of packets> <base wait time> <router drop rate in percentage>
  all parameters should be numbers
  
  size of each packet increases 1 by 1, up to <number of packets>. routed/forwarded in slow start fashion.
