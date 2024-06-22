clear all;
close all

t=0:0.0001:2;
f1=1; % msg frequency
f2=20; % sawtooth frequency

mssg=0.9*sin(2*pi*f1*t);
subplot(5,1,1);
plot(t,mssg);
title('Message Signal (22071A04D4)')
axis([0 1 -1 1]);

%generation of sawtooth
sa = sawtooth(2*pi*f2*t);
subplot(5,1,2);
plot(t,sa)
title('Sawtooth Waveform (22071A04D4)')
axis([0 1 -1 1]);

%Pulse Width Modulation
pwm=(mssg>sa);
subplot(5,1,3);
plot(t,pwm)
axis([min(t),max(t),0,2])
title('Pulse Width Modulation (22071A04D4)')
axis([0 1 -0.5 1.5]);

%%PPM generation
x1=~pwm; %inverter output
y1=diff(x1); % differentiator output
ppm=zeros(1,length(y1));
k=1;
while k<length(y1)
    if y1(1,k) ==1
        ppm(1,k:k+49)=ones(1,50); %pulse of width 50*0.0001=0.005 sec
        k=k+49;
    else k=k+1;
    end
end
subplot(5,1,4)
plot(0:0.0001:1.9999,ppm)
axis([min(t),max(t),0,2])
title('Pulse Position Modulation (22071A04D4)');
axis([0 1 -0.5 1.5]);