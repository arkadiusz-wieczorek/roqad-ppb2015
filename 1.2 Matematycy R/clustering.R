print(commandArgs(TRUE))

# wczytanie csv i wyjęcie URL deviców, które chcemy

# te które chcemy wyjąć - pierwsza kolumna to muszą być ID device'ów (learning set)
result <- read.csv(commandArgs(TRUE)[1]) 
result["cluster"] <- NA

# wszystkie device z URL ze zbioru uczącego pierwsza kolumna to device_id, a druga to lista urli
learning_url <- read.csv(commandArgs(TRUE)[2])


balURLlist <- matrix(0, ncol = 2, nrow = nrow(result))


print("clustering - step 1/3...")

for (i in 1:nrow(result)) {
  for (j in 1:nrow(learning_url)) {
    if (do.call("paste", result[i,][1]) == do.call("paste", learning_url[j,][1])) {
      balURLlist[i,1] <- do.call("paste", learning_url[j,][1])
      balURLlist[i,2] <- do.call("paste", learning_url[j,][2])
      break
    }
  }
  print(i/nrow(result)*100)
  flush.console()
}

URLmatrix <- balURLlist

# funkcje

naliste <- function(i) {
  d=nchar(as.character(URLmatrix[i,2]))-1
  x= substring(URLmatrix[i,2],2,d)
  list <- as.list(strsplit(x, ",")[[1]])
  list <- unique(list)
  return(list)
}

distance <- function(i,j) {
  naliste(i)
  naliste(j)
  score <- length(intersect(naliste(i),naliste(j)))/min(length(naliste(i)),length(naliste(j)))
  return(score)
}

custom.dist <- function(n, my.function) {
  n <- length(c(1:n))
  mat <- matrix(0, ncol = n, nrow = n)
  colnames(mat) <- rownames(mat) <- URLmatrix[1:n, 1]
  for(i in 1:nrow(mat)) {
    for(j in 1:ncol(mat)) {
      mat[i,j] <- 1 - my.function(i,j)
    }
    flush.console()}
  return(mat)
}

# macierz odleglosci

dis <- custom.dist(nrow(URLmatrix), distance)


# clustering

dist.matrix <- dist(dis, method = "euclidean", diag = FALSE, upper = FALSE, p = 2)

hfit<- hclust(dist.matrix, method = "complete", members = NULL)
plot(hfit)
cl <- rect.hclust(hfit, floor(sqrt(nrow(URLmatrix)/2))) # l. clustrow = pierw n/2
cl

# device-cluster indentification list

clusters <- matrix(0, nrow =nrow(URLmatrix) , ncol = 2)

print("Clustering - step 2/3...")

for(i in 1:nrow(clusters)) {
  clusters[i,1] <- colnames(dis)[i]
  print(i/nrow(clusters)*100)
}

print("Clustering - step 3/3...")

for(i in 1:nrow(clusters)) {
  for(j in 1:floor(sqrt(nrow(URLmatrix)/2))) {
    if(clusters[i,1] %in% names(cl[[j]])) {
      clusters[i,2] <- j }
  }
  print(i/nrow(clusters)*100)
}

result$cluster = clusters[,2]

# export to csv device-cluster indentification list

write.table(result, file = commandArgs(TRUE)[3], sep = " , ", row.names = FALSE, col.names = TRUE)
