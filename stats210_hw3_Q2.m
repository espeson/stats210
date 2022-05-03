grid=[]
for i=1:150
    a=randn(i)+1
    x=mean(mean(a))
    grid(i)=x
end
plot([1:150],grid)
