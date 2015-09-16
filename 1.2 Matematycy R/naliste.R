naliste <- function(i) {
  d=nchar(as.character(col[i,]))-1
  x= substring(col[i,],2,d)
  list <- as.list(strsplit(x, ",")[[1]])
   list <- unique(list)
  return(list)
}

