x = linspace(0,20,10000)
plot(x,x.^2,'r-')
hold on
plot(x,x.*log(x),'g-')
plot(x,x,'b-')
plot(x,exp(x),'k-')
plot(x,log(x),'c-')
xlim([0 20])
ylim([0 100])
legend('x^2','xlogx','x','e^x','log(x)')

