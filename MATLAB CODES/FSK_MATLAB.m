clear all; close all;
fs=1000;
fc1=80;
fc2=40;
fm=10;
sgtitle('Frequency Shift Keying - 22071A04D4');
t=-1:1/fs:1;

am=3;
c1=am*sin(2*pi*fc1*t);
c2=(am/2)*sin(2*pi*fc2*t);

m1=(am/2)*square(2*pi*fm*t)+(am/2);
m2=(am/2)*square(-2*pi*fm*t)+(am/2);


z=(c1.*m1 + c2.*m2);
subplot(4,1,1);
plot(t,c1);
xlabel("time");
ylabel("amplitude");
title("Carrier 1");
subplot(4,1,2);
plot(t,c2);
xlabel("time");
ylabel("amplitude");
title("Carrier 2");
subplot(4,1,3);
plot(t,m1);
xlabel("time");
ylabel("amplitude");
title("Data I/P");
axis([min(t),max(t),min(m1)-0.5,max(m1)+0.5])
subplot(4,1,4);
plot(t,z);
xlabel("time");
ylabel("amplitude");
title("FSK Signal");