# NCBIsummary
This script can get your ENSEMBL ID from your different expression and get summary of those IDs from NCBI
## Usage
You just need to provide the `txt` file of you different expression transcript IDs, which are divided by newline character. For example
```
ENSAMEG00000003844
ENSAMEG00000022797
ENSAMEG00000022987
ENSAMEG00000022842
ENSAMEG00000004331
ENSAMEG00000021257
ENSAMEG00000005216
ENSAMEG00000019807
ENSAMEG00000005788
```

and the command of using the script is very easy.
`python NCBI.py DEG.txt >> output.txt`

## Important
The version of python must be 3 or higher
