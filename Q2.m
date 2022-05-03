n=100000;%times to throw the needle
count_underline=0;%number of point under the line
for i=1:n
    x=rand;
    y=rand;
    if y<1/(1+x)
        count_underline=count_underline+1;
    end
end
Area=(count_underline/n);