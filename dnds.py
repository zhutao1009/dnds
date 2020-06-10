import copy
from aa import codons
import math
import sys

def split_seq(seq,n):
    s=[]
    for i in range(0,len(seq),n):
        s.append(seq[i:i+n])
    return s

def trans_2_condon(seq):
    codons_list=[]
    for base in split_seq(seq,3):
        codons_list.append(codons[base])
    return codons_list

def diff(codon1,codon2):
    df=[]
    for base in range(0,3):
        if codon1[base]!=codon2[base]:
            df.append(base)
    return df

def trans(l):
    if len(l)==1:
        return [l]
    if len(l)==2:
        return [
            l,
            [l[1],l[0]]
        ]
    if len(l)==3:
        return [l,
[l[0],l[2],l[1]],
[l[1],l[0],l[2]],
[l[1],l[2],l[0]],
[l[2],l[0],l[1]],
[l[2],l[1],l[0]]
]

def sd_nd(codon1,codon2):
    snp_pos=diff(codon1,codon2)
    pathway=trans(snp_pos)
    combine=''
    for aa in pathway:
        new_condon=copy.deepcopy(codon1)
        combine=combine+''.join(new_condon)
        for base in aa:
            new_condon[base]=codon2[base]
            combine=combine+''.join(new_condon)
    return (combine)

def count_diff(aa_list):
    count=0
    for i in range(0,len(aa_list)-1):
        if aa_list[i]!=aa_list[i+1]:
            count+=1
    return count

def sd_nd_cal(combine):
    nd=0
    pep=trans_2_condon(combine)
    if len(pep)==2:
        if pep[0]==pep[1]:
            return [1,0]
        else:
            return [0,1]
    elif len(pep)==6:
        peplist=split_seq(pep,2)
        for i in peplist:
            nd+=count_diff(i)
        return [(4-nd)/2,nd/2]
    else:
        peplist=split_seq(pep,4)
        for i in peplist:
            nd+=count_diff(i)
            #print (i,count_diff(i))
        return [(18-nd)/6,nd/6]

def test_syno(codon1,codon2):
    if codons[codon1]==codons[codon2]:
        return 1
    else:
        return 0

def S_n(codon):
    base={'A','G','C','T'}
    s_num=0
    for b in [0,1,2]:
        other_base=base-{codon[b]}
        for newbase in other_base:
            new_condon=codon[:b] + newbase + codon[b + 1:]
            s_num+=test_syno(codon,new_condon)
    return (s_num)


def s_n_seq(seq):
    condon_list=split_seq(seq,3)
    sd=0
    for i in condon_list:
        sd+=S_n(i)
    nd=len(condon_list)*3-sd/3
    return [sd/3,nd]



def ds_dn_seq(seq1,seq2):
    condon_list1=split_seq(seq1,3)
    condon_list2=split_seq(seq2,3)
    sd_nd_val=[0,0]
    for cond in range(0,len(condon_list1)):
        c1=condon_list1[cond]
        c2=condon_list2[cond]
        if c1==c2:
            pass
        else:
            xy=sd_nd(list(c1),list(c2))
            sd_nd_exp2=sd_nd_cal(xy)
            sd_nd_val[0]+=sd_nd_exp2[0]
            sd_nd_val[1]+=sd_nd_exp2[1]
    return sd_nd_val

def dnds(seq1,seq2):
    assert len(seq1)==len(seq2),'Fatal err:length(seq1)!=length(seq2)'
    assert len(seq1)%3==0,'Fatal err:The length of input seq is not divisible by 3'
    assert seq1!=seq2,'Fatal err:2 sequence is same'
    sdnd1=s_n_seq(seq1)
    sdnd2=s_n_seq(seq2)
    sdnd=[(sdnd1[0]+sdnd2[0])/2,(sdnd1[1]+sdnd2[1])/2]
    sd=ds_dn_seq(seq1,seq2)
    ps=sd[0]/sdnd[0]
    pn=sd[1]/sdnd[1]
    print ('pn=%f,ps=%f'%(pn,ps))
    ds=-0.75*math.log(1-(4*ps)/3)
    dn=-0.75*math.log(1-(4*pn)/3)
    print ('dn=%f,ds=%f'%(dn,ds))
    print ('dn/ds=%f'%(dn/ds))
    return dn/ds

def readfasta(input):
    with open(input,'r') as f:
        fasta={}
        for line in f:
            line = line.strip()
            if line[0] == '>':
                h = line[1:].split(" ")
                header=h[0]
            else:
                sequence = line
                fasta[header] = fasta.get(header,'') + sequence
    return fasta

if __name__ == "__main__":
    fa=readfasta(sys.argv[1])
    assert len(fa)==2,'Fatal err:please check the sequence file'
    seq1=list(fa.values())[0]
    seq2=list(fa.values())[1]
    dnds(seq1,seq2)