clear all 
close all
t=-10:0.01:10; T=4; fm=1/T;
x=sin(pi*fm*t)+cos(2*pi*fm*t); 
subplot(3,2,1);
plot(t,x); 
xlabel("time"); 
ylabel("amp"); 
title("Continuous Time Signal(22071A04G4)");

fs1=1.2*fm;
fs2=2*fm;
fs3=8*fm;

n1=-4:1:4; 
x1=sin(pi*fm*n1/fs1)+cos(2*pi*fm*n1/fs1); 
subplot(3,2,2); 
stem(n1,x1);
hold on; 
subplot(3,2,2);
plot(n1,x1);
xlabel("time");
ylabel("amp"); 
title("Overlap(22071A04G4)");

n2=-5:1:5;
x2=sin(pi*fm*n2/fs2)+cos(2*pi*fm*n2/fs2);
subplot(3,2,3); 
stem(n2,x2); hold on; 
subplot(3,2,3);
plot(n2,x2); 
xlabel("time"); 
ylabel("amp"); 
title("Nyquiest(22071A04G4)");  

n3=-20:1:20; 
x3=sin(pi*fm*n3/fs3)+cos(2*pi*fm*n3/fs3); 
subplot(3,2,4); 
stem(n3,x3);
hold on
plot(n3,x3); 
xlabel("time"); 
ylabel("amp"); 
title("Sampling(22071A04G4)");

subplot(3,2,5); 
plot(n3,x3); 
xlabel("time"); 
ylabel("amp"); 
title("Reconstruction(22071A04G4)");

sgtitle("SAMPLING THEOREM - 22071A04G4") 
fontsize(12,"points");