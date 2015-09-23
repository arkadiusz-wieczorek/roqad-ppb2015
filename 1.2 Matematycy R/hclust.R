hfit <- hclust(mama, method = "average", members = NULL)
plot(hfit)
cl <- rect.hclust(hfit, 25) # l. clustrow = pierw n/2
cl
