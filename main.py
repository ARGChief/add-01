from machine import Pin
from time import sleep 
Pin1 = Pin (28, Pin.IN)
Pin2 = Pin (27, Pin.IN)
Led1 = Pin (1, Pin.OUT)
Led2 = Pin (2, Pin.OUT)

while True:



  if Pin1.value () == 1:
    Led1.value(1)

  if Pin1.value () == 0:
   Led1.value (0)
  
  if Pin2.value () == 1:
    if Led2.value () == 1:
      Led2.value (0)
      sleep (0.5)
    elif Led2.value () == 0:
      Led2.value (1)
      sleep (0.5)


  