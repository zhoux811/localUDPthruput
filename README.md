# localUDPthruput

run driver in terminal: 
  python driver.py \<number of packets\> \<base wait time\> \<router drop rate in percentage\>
  <br>
  all parameters should be numbers
  <br><br>
  size of each packet increases 1 by 1, up to \<number of packets\>. routed/forwarded in slow start fashion.
  <br><br>
  For example:
  <br>
  command: "python driver.py 150 0.2 1"
  <br>
  means:
  <br>
  SENDER sends 150 packets from size 1 byte to 150 bytes to router. router randomly drop 1 packet for 1% probability. then forwards data to RECEIVER. if sender detects an unordered or lost packet, ask SENDER to send again. transmitting UDP sockets.
