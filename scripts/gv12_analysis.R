library( tidyverse )
library( ggplot2 )
setwd("~/Documents/Uni/DataScience/Sem2/BIII/A3/scripts")

data = read.csv("mvu_oks_new.csv", sep = ";", header = TRUE)
x<- data$ok
h<-hist(x, breaks=10, col="red", xlab="Ok Status Measurements", ylab="Number of parts",
        main="MicroVu Ok") 
xfit<-seq(min(x),max(x),length=40) 
yfit<-dnorm(xfit,mean=mean(x),sd=sd(x)) 
yfit <- yfit*diff(h$mids[1:2])*length(x) 
lines(xfit, yfit, col="blue", lwd=2)

x<- data$nok
h<-hist(x, breaks=5, col="red", xlab="Nok Status Measurements", ylab="Number of parts",
        main="MicroVu Nok") 
xfit<-seq(min(x),max(x),length=40) 
yfit<-dnorm(xfit,mean=mean(x),sd=sd(x)) 
yfit <- yfit*diff(h$mids[1:2])*length(x) 
lines(xfit, yfit, col="blue", lwd=2)

ord = data[order(data$cn),]
barplot(ord$nok, ylim=c(0,5), names.arg=data$cn)

data = read.csv("qr_codes.csv", sep = ";", header = TRUE)
bar_change = c(128, 184, 36, 91)
param_change = c(125,128,130,132,135,136,137,140,142,144,147,155,162,164,174,178,181,185,187,191,192,195,5,7,8,25,38,62,73,75,94,110)

for(i in 1:length(bar_change)) {
  data[data$qrcode==bar_change[i],]
}

data = read.csv("prod_measurements2.csv", sep = ";", header = TRUE)

