clear all;
close all;

fm=10;
fc=100;
fs=1000;
t=0:1/fs:1; %Time Period

m=cos(2*pi*fm.*t);  %Message Signal with 0 phase shift
mc=sin(2*pi*fm.*t); %Message Signal with 90 phase shift

c=cos(2*pi*fc.*t);  %Carrier Signal with 0 phase shift
cc=sin(2*pi*fc.*t); %Carrier Signal with 90 phase shift

fx=m.*c;    %DSBSC Signal
fy=mc.*cc;  %DSBSC Signal

s1 = fx-fy; %LSB Signal
s2 = fx+fy; %USB Signal

subplot(3,1,1);
plot(t,m);
xlabel("time");
ylabel("amplitude");
title("Message Signal-22071A04G4");


subplot(3,1,2);
plot(t,mc);
xlabel("time");
ylabel("amplitude");
title("Message Signal with phaseshift-22071A04G4");

subplot(3,1,3);
plot(t,c);
xlabel("time");
ylabel("amplitude");
title("Carrier Signal-22071A04G4");
sgtitle("SSBSC - 22071A04G4");
fontsize(12,"points");

figure;

subplot(3,1,1);
plot(t,cc);
xlabel("time");
ylabel("amplitude");
title("Carrier Signal with phaseshift-22071A04G4");

subplot(3,1,2);
plot(t,fx);
xlabel("time");
ylabel("amplitude");
title("DSBSC Signal(fx)");

subplot(3,1,3);
plot(t,fx);
xlabel("time");
ylabel("amplitude");
title("DSBSC Signal(fy)");
fontsize(12,"points");
figure;

subplot(3,1,1);
plot(t,s1);
xlabel("time");
ylabel("amplitude");
title("Lower Side Band Signal-22071A04G4");

subplot(3,1,2);
plot(t,s2);
xlabel("time");
ylabel("amplitude");
title("Upper Side Band Signal-22071A04G4");

d=s1.*cos(2*pi*fc.*t);
[b,a]=butter(5,fm/(fs/2));
demod=filter(b,a,d);

subplot(3,1,3);
plot(t,demod);
xlabel("time");
ylabel("amplitude");
title("Demodulated Signal-22071A04G4");

fontsize(12,"points");