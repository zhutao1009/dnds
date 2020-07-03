

# **dnds**: calculate the dn/ds (also include pn and ps) value of CDS.  

# Installation
```shell
$git clone https://github.com/zhutao1009/dnds.git
```
# Usage
## Usage 1:   
```python
>>>from dnds import dnds   
>>>seq1='CTGTGCACT'  
>>>seq2='CTATCCGCT'  
>>>dnds_test=dnds(seq1,seq2)  
pn=0.315789,ps=0.375000  
dn=0.409908,ds=0.519860  
dn/ds=0.788496  
>>>print (dnds_test)  
0.788496  
```
## Usage 2:   
```shell
$cat demo.fa  
>NP_000006.1_1
ATGGACATTGAAGCATATTTTGAAAGAATTGGCTATAAGAACTCTAGGAACAAATTGGACTTGGAAACATTAACTGACATTCTTGAGCACCAGATCCGGGCTGTTCCCTTTGAGAACCTTAACATGCATTGTGGGCAAGCCATGGAGTTGGGCTTAGAGGCTATTTTTGATCACATTGTAAGAAGAAACCGGGGTGGGTGGTGTCTCCAGGTCAATCAACTTCTGTACTGGGCTCTGACCACAATCGGTTTTCAGACCACAATGTTAGGAGGGTATTTTTACATCCCTCCAGTTAACAAATACAGCACTGGCATGGTTCACCTTCTCCTGCAGGTGACCATTGACGGCAGGAATTACATTGTCGATGCTGGGTCTGGAAGCTCCTCCCAGATGTGGCAGCCTCTAGAATTAATTTCTGGGAAGGATCAGCCTCAGGTGCCTTGCATTTTCTGCTTGACAGAAGAGAGAGGAATCTGGTACCTGGACCAAATCAGGAGAGAGCAGTATATTACAAACAAAGAATTTCTTAATTCTCATCTCCTGCCAAAGAAGAAACACCAAAAAATATACTTATTTACGCTTGAACCTCGAACAATTGAAGATTTTGAGTCTATGAATACATACCTGCAGACGTCTCCAACATCTTCATTTATAACCACATCATTTTGTTCCTTGCAGACCCCAGAAGGGGTTTACTGTTTGGTGGGCTTCATCCTCACCTATAGAAAATTCAATTATAAAGACAATACAGATCTGGTCGAGTTTAAAACTCTCACTGAGGAAGAGGTTGAAGAAGTGCTGAAAAATATATTTAAGATTTCCTTGGGGAGAAATCTCGTGCCCAAACCTGGTGATGGATCCCTTACTATT  
>NP_000006.1_2
ATGGACATCGAAGCATACTTTGAAAGGATTGGTTACAAGAACTCAGTGAATAAATTGGACTTAGCCACATTAACTGAAGTTCTTCAGCACCAGATGCGAGCAGTTCCTTTTGAGAATCTTAACATGCATTGTGGAGAAGCCATGCATCTGGATTTACAGGACATTTTTGACCACATAGTAAGGAAGAAGAGAGGTGGATGGTGTCTCCAGGTTAATCATCTGCTGTACTGGGCTCTGACCAAAATGGGCTTTGAAACCACAATGTTGGGAGGATATGTTTACATAACTCCAGTCAGCAAATATAGCAGTGAAATGGTCCACCTTCTAGTACAGGTGACCATCAGTGACAGGAAGTACATTGTGGATTCCGCCTATGGAGGCTCCTACCAGATGTGGGAGCCTCTGGAATTAACATCTGGGAAGGATCAGCCTCAGGTGCCTGCCATCTTCCTTTTGACAGAGGAGAATGGAACCTGGTACTTGGACCAAATCAGAAGAGAGCAGTATGTTCCAAATGAAGAATTTGTTAACTCAGACCTCCTTGAAAAGAACAAATATCGAAAAATCTACTCCTTTACTCTTGAGCCCCGAGTTATCGAGGATTTTGAATATGTGAATAGCTATCTTCAGACATCGCCAGCATCTGTGTTTGTAAGCACATCGTTCTGTTCCTTGCAGACCTCGGAAGGGGTTCACTGTTTAGTGGGCTCCACCTTTACAAGTAGGAGATTCAGCTATAAGGACGATGTAGATCTGGTTGAGTTTAAATATGTGAATGAGGAAGAAATAGAAGATGTACTGAAAACCGCATTTGGCATTTCTTTGGAGAGAAAGTTTGTGCCCAAACATGGTGAACTAGTTTTTACTATT 

$python dnds.py demo.fa  
pn=0.150498,ps=0.448961  
dn=0.167981,ds=0.684625  
dn/ds=0.245362  
```
The [KaKs_Calculator](https://sourceforge.net/projects/kakscalculator2/) result:
| Sequence      | Method | Ka        | Ks        | Ka/Ks     | P\-Value\(Fisher\) | Length | S\-Sites | N\-Sites | Fold\-Sites\(0:2:4\) | Substitutions | S\-Substitutions | N\-Substitutions | Fold\-S\-Substitutions\(0:2:4\) | Fold\-N\-Substitutions\(0:2:4\) | Divergence\-Time | Substitution\-Rate\-Ratio\(rTC:rAG:rTA:rCG:rTG:rCA/rCA\) | GC\(1:2:3\)                              | ML\-Score | AICc | Akaike\-Weight | Model |
|---------------|--------|-----------|-----------|-----------|--------------------|--------|----------|----------|----------------------|---------------|------------------|------------------|---------------------------------|---------------------------------|------------------|----------------------------------------------------------|------------------------------------------|-----------|------|----------------|-------|
| NP\_000006\.1 | NG     | 0\.163702 | 0\.684541 | 0\.239141 | 1\.54E\-17         | 870    | 192\.31  | 677\.69  | NA                   | 186           | 86\.3333         | 99\.6667         | NA                              | NA                              | 0\.278831        | 1:1:1:1:1:1                                              | 0\.422989\(0\.468966:0\.32931:0\.47069\) | NA        | NA   | NA             | NA    |



# Reference:  
M Nei, T Gojobori, Simple methods for estimating the numbers of synonymous and nonsynonymous nucleotide substitutions., Molecular Biology and Evolution, Volume 3, Issue 5, September 1986, Pages 418–426, https://doi.org/10.1093/oxfordjournals.molbev.a040410  


**Warning**: this program was tested based on python3
