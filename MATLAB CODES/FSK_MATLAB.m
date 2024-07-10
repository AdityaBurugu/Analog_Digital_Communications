
clear all; close all;
sgtitle('Frequency Shift Keying - 22071A04D4');
fs=1000;
t=0:1/fs:10;
f1=5;
f2=2;
fm=0.5;
m=0.5.*square(2*pi*fm*t)+0.5;

subplot(5,1,1);
plot(t,m);
xlabel('Time');
ylabel('Amplitude');
title('Unipolar NRZ Message Signal');
axis([min(t) max(t) min(m)-0.5 max(m)+0.5]); 

x1=cos(2*pi*f1*t);
subplot(5,1,2);
plot(t,x1);
xlabel('Time');
ylabel('Amplitude');
title('Carrier Signal 1');

x2=cos(2*pi*f2*t);
subplot(5,1,3);
plot(t,x2);
xlabel('Time');
ylabel('Amplitude');
title('Carrier Signal 2');

y1=m.*x1;
y2=not(m).*x2;
y3=y1+y2;
subplot(5,1,4);
plot(t,y3);
xlabel('Time');
ylabel('Amplitude');
title('FSK Modulated Signal');

d1=y3.*x1;
d2=y3.*x2;
[b1,a1]=butter(1,f1/fs,'low');
[b2,a2]=butter(1,f2/fs,'low');
de1=filter(b1,a1,d1);
de2=filter(b2,a2,d2);
dem1=de1-de2;
demo=zeros(1,length(t));
for i =1:length(t)
if(dem1(i)>0)
demo(i)=1;
else
demo(i)=0;
end
end
subplot(5,1,5);
plot(t,demo);
xlabel('Time');
ylabel('Amplitude');
title('Demodulated Signal');
axis([min(t) max(t) min(demo)-0.5 max(demo)+0.5]); 