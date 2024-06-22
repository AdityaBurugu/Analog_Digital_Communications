clear all
close all

% Generation of PCM
% PCM signal generation
f=2;
a=3;
fs=20*f;
t= 0:1/fs:2;
x=a*sin(2*pi*f*t);
subplot(5,1,1)
plot(t,x)
title ('Analog signal-22071A04D4');
xlabel('Time Axis');
ylabel('Amplitude');
subplot(5,1,2)
stem(t,x);

% level shifting
x1=x+a;
l=length(x1);
% quantization
q_op=round(x1);

subplot(5,1,3)
plot(t,q_op)
title ('Quantized signal-22071A04D4');
xlabel('Time Axis');
ylabel('Amplitude');

% encoder
enco= dec2bin(q_op);
k=1;
code=zeros(1,l);
for i=1:l
for j=1:3
code(k)= enco(i,j)-48;
k=k+1;
end
end
subplot(5,1,4),stairs(code);
axis([0 243 0 2]);
title('Encoded Signal-22071A04D4');
xlabel('Time Axis');
ylabel('Amplitude');
% receiver
deco= bin2dec(enco);
% shifting amplitude level
xr=deco-a;
%plotting
subplot(5,1,5)
plot(t,xr,'r')
title('Decoded Signal-22071A04D4')
xlabel('Time Axis');
ylabel('Amplitude');