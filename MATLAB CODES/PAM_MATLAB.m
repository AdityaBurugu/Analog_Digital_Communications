fs=1000;
T=1/fs;
t=0:T:pi;  %Time Period

a=1;
fm=1;
fc=10;
c = 0.5.*square(2*pi*fc.*t)+0.5;
m = a.*sin(2*pi*fm.*t);
y = m.*c;

u=[];
for i=1:length(y)
if y(i)==0
    u=[u,y(i)];
else 
    u=[u,y(i)+2];
end
end

dmod = y.*c;
filter = fir1(200,fm/fs,'low');
og = conv(filter,dmod);

subplot(5,1,1);
plot(t,m);
xlabel('Time');
ylabel('Amplitude');
title('Sinusoidal Signal-22071A04G4');

subplot(5,1,2);
plot(t,c);
xlabel('Time');
ylabel('Amplitude');
title('Carrier Signal-22071A04G4');
axis([min(t),max(t), min(c)-0.5,max(c)+0.5]);

subplot(5,1,3);
plot(t,y);
xlabel('Time');
ylabel('Amplitude');
title('PAM Bipolar Waveform-22071A04G4');
axis([min(t),max(t), min(y)-0.2,max(y)+0.2]);

subplot(5,1,4);
plot(t,u);
xlabel('Time');
ylabel('Amplitude');
title('PAM Unipolar Waveform-22071A04G4');
axis([min(t),max(t), min(u),max(u)+0.5]);

t=0:1/((length(og))-1):1;
subplot(5,1,5);
plot(t,og);
xlabel('Time');
ylabel('Amplitude');
title('PAM Demodulated Waveform-22071A04G4');

sgtitle("PAM - 22071A04G4") 
fontsize(12,"points");