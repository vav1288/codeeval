args <- commandArgs(trailingOnly=TRUE)
test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n', fixed=TRUE)

for (test in test.cases) {

    if (length(test) > 0) {
        data <- strsplit(test, ';', fixed=TRUE)[[1]]
        N <- as.numeric(data[1])
        numbers <- as.numeric(strsplit(data[2], ' ', fixed=TRUE)[[1]])
        
        if (length(numbers) < N){
            cat('0\n')
            next
        }
        
        current_sum <- sum(numbers[1:N])
        best_sum <- max(0, current_sum)
        
        if (N<length(numbers)){
            for (i in (N+1):length(numbers)){
                current_sum <- current_sum + numbers[i] - numbers[i-N]
                if (current_sum > best_sum){
                    best_sum <- current_sum
                }
            }
        }
        cat(best_sum, '\n')
        
    }

}


        
        
        

        
