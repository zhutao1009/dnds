

# **dnds**: calculate the dn/ds (also include pn and ps) value of CDS.  


# Usage
## Usage 1:   

\>>>from dnds import dnds   
\>>>seq1='CTGTGCACT'  
\>>>seq2='CTATCCGCT'  
\>>>dnds_test=dnds(seq1,seq2)  
pn=0.315789,ps=0.375000  
dn=0.409908,ds=0.519860  
dn/ds=0.788496  
\>>>print (dnds_test)  
0.788496  

## Usage 2:   
$python dnds.py demo.fa  
pn=0.315789,ps=0.375000  
dn=0.409908,ds=0.519860  
dn/ds=0.788496  

# Reference:  
M Nei, T Gojobori, Simple methods for estimating the numbers of synonymous and nonsynonymous nucleotide substitutions., Molecular Biology and Evolution, Volume 3, Issue 5, September 1986, Pages 418–426, https://doi.org/10.1093/oxfordjournals.molbev.a040410  


**Warning**: this program was tested based on python3
