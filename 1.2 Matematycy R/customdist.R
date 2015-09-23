custom.dist <- function(n, my.function) {
  n <- length(c(1:n))
  mat <- matrix(0, ncol = n, nrow = n)
  colnames(mat) <- rownames(mat) <- listaURL[1][0:n,]
  for(i in 1:nrow(mat)) {
    for(j in 1:ncol(mat)) {
      mat[i,j] <- my.function(i,j)
    }
    print(i)
    flush.console()}
  return(mat)
}

