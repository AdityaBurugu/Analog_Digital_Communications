clear all; 
close all;

sgtitle("Amplitude Shift Keying - 22071A04D4");
fs=1000;
fm=1;
fc=10;
t= 0:1/fs:2;
am=2;
c=am*sin(2*pi*fc*t);
m=am/2*square(2*pi*fm*t)+(am/2);
s=m.*c;

subplot(4,1,1);
plot(t,m);
xlabel("time");
ylabel("amplitude");
title("Data I/P");
axis([min(t),max(t),min(m)-0.5,max(m)+0.5])

subplot(4,1,2);
plot(t,c);
xlabel("time");
ylabel("amplitude");
title("CarrierSignal");
axis([min(t),max(t),min(c)-0.5,max(c)+0.5])

subplot(4,1,3);
plot(t,s);
xlabel("time");
ylabel("amplitude");
title("ASK Signal");
axis([min(t),max(t),min(s)-0.5,max(s)+0.5])

x=s.*c;
d=sign(x);

subplot(4,1,4);
plot(t,d);
xlabel("time");
ylabel("amplitude");
title("Demodulated Signal")
axis([min(t),max(t),min(d)-0.5,max(d)+0.5])
