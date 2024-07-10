clc
close all
clear all

sgtitle('Phase Shift Keying - 22071A04D4');

fs=1000;
t=0:1/fs:10;
fm = 0.5;
x=square(2*pi*fm.*t);
subplot(4,1,1);
plot(t,x)
title('Polar NRZ Signal');
xlabel('Time');
ylabel('Amplitude');

fc=2;
c = cos(2*pi*fc*t);
subplot(4,1,2);
plot(t,c);
title('Carrier Signal');
xlabel('Time');
ylabel('Amplitude');

s = x.*c;
subplot(4,1,3);
plot(t,s);
title('PSK Modulated Signal');
xlabel('Time');
ylabel('Amplitude');

d=sign(s.*c);
subplot(4,1,4);
plot(t,d);
title('Demodulated Signal');
xlabel('Time');
ylabel('Amplitude');