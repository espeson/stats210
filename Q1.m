length=5;%length of the needle
distance=10;%distance between two paralle lines
n2=100;
n3=1000;
n4=10000;
n5=100000;%times to throw the needle
count2=0;%times of crossing
count3=0;%times of crossing
count4=0;%times of crossing
count5=0;%times of crossing
for i=1:n2
    x=(distance/2)*rand;
    theta=pi*rand;
    if x<(length/2)*sin(theta)
        count2=count2+1;
    end
end
Pi2=n2/count2;
for i=1:n3
    x=(distance/2)*rand;
    theta=pi*rand;
    if x<(length/2)*sin(theta)
        count3=count3+1;
    end
end
Pi3=n3/count3;
for i=1:n4
    x=(distance/2)*rand;
    theta=pi*rand;
    if x<(length/2)*sin(theta)
        count4=count4+1;
    end
end
Pi4=n4/count4;
for i=1:n5
    x=(distance/2)*rand;
    theta=pi*rand;
    if x<(length/2)*sin(theta)
        count5=count5+1;
    end
end
Pi5=n5/count5;
xaxis=[n2 n3 n4 n5];
yaxis=[Pi2 Pi3 Pi4 Pi5];
semilogx(xaxis,yaxis)
grid on