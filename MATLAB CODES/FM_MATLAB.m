close all;
clear all;

fs = 1000;
t = 0:1/fs:2;   %Time Period

ac = 1;
am = 1;

fc = 10;
fm = 1;

wc = 2*pi*fc;
wm = 2*pi*fm;

c = ac.*cos(wc.*t); %Carrier Signal
m = am.*sin(wm.*t); %Message Signal

subplot(3,2,1);
plot(t,m);
title("Message Signal-22071A04G4");
ylabel('amplitude');
xlabel("time");

subplot(3,2,2);
plot(t,c);
title("Carrier Signal-22071A04G4");
ylabel('amplitude');
xlabel("time");

b = 0.5;
s1 = ac.*cos(wc.*t +b.*m);  %Single Tone FM(Narrow Band)
subplot(3,2,3);
plot(t,s1);
title("Narrow Band FM-22071A04G4");
ylabel('amplitude');
xlabel("time");

b = 5;
s2 = ac.*cos(wc.*t +b.*m);  %Single Tone FM(Wide Band)
subplot(3,2,4);
plot(t,s2);
title("Wide Band FM-22071A04G4");
ylabel('amplitude');
xlabel("time");    

%demodulation - narrow band fm
d = s1.* c;
d1 = fmdemod(s1,fc,fs,fc+2);
[b,a] = butter(2,2*fm/fs);
z = filter(b,a,d1);
subplot(3,2,5)
plot(t,z);
title("Demodulation -Narrow band FM-22071A04G4");
ylabel('amplitude');
xlabel("time");

%demodulation - wide band fm
d = s2.* c;
d2 = fmdemod(s2,fc,fs,fc);
[b,a] = butter(2,2*fm/fs);
z = filter(b,a,d2);
subplot(3,2,6)
plot(t,z);
title("Demodulation - Wide band FM-22071A04G4");
ylabel('amplitude');
xlabel("time");

sgtitle("FM - 22071A04G4") 
fontsize(12,"points");