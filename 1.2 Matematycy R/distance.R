distance <- function(i,j) {
  naliste(i)
  
  naliste(j)
  
  score <- length(intersect(naliste(i),naliste(j)))/min(length(naliste(i)),length(naliste(j)))
  
  return(score)
}

