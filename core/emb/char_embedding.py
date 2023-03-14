from base_embedding import BaseEmbedding

class CharEmbedding(BaseEmbedding):
    def __init__(
            self,
            model_name='bert-large-cased',
            seed=42,
            **kwarg
        ) -> None:
        super().__init__(model_name, seed, **kwarg) # type: ignore


def main():
    import string
    import numpy as np
    np.set_printoptions(
        precision=5, 
        threshold=5
    )
    ce = CharEmbedding()
    characters = list(string.printable)
    embeddings = ce.embed_input(characters)
    characters[-6] = " "
    characters[-5] = "\\n"
    characters[-4] = "\\t"
    characters[-3] = "\\r"
    characters[-2] = "\\v"
    characters[-1] = "\\f"
    for idx, character in enumerate(characters):
        print(character, embeddings[idx])


if __name__ == "__main__":
    main()

# 0 [-0.0089  -0.29244 -0.11111 ... -0.19998 -0.24979 -0.13677]
# 1 [-0.12683 -0.35149  0.15281 ... -0.24885 -0.38195 -0.05897]
# 2 [-0.38673 -0.57783  0.04163 ... -0.17759 -0.05834 -0.02157]
# 3 [-0.37558 -0.42487  0.14551 ... -0.34655 -0.20865 -0.02804]
# 4 [-0.38411 -0.59139  0.1912  ... -0.28363 -0.33586  0.06489]
# 5 [-0.34705 -0.46374  0.22425 ... -0.48916 -0.31353  0.04094]
# 6 [-0.46146 -0.53709  0.11905 ... -0.57137 -0.36377 -0.13948]
# 7 [-0.42331 -0.37839  0.37446 ... -0.46227 -0.29055  0.0756 ]
# 8 [-0.46041 -0.50035  0.45026 ... -0.32907 -0.20871 -0.02769]
# 9 [-0.45973 -0.46431  0.33501 ... -0.46803  0.04425  0.0906 ]
# a [ 0.06934 -0.71711  0.36821 ...  0.2557   0.37772  0.15829]
# b [-0.37766 -0.57014  0.4322  ... -0.02725 -0.18119  0.0864 ]
# c [ 0.01312 -0.38436  0.24671 ...  0.48916 -0.21185  0.28957]
# d [-0.36905 -0.24992  0.49686 ...  0.29001  0.09609 -0.04471]
# e [-0.20921 -0.37015  0.25017 ... -0.11485  0.10415  0.4101 ]
# f [-0.18038 -0.57123  0.46613 ... -0.10305  0.07275  0.16509]
# g [-0.43355 -0.28083  0.53959 ...  0.08147 -0.08117  0.42862]
# h [-0.41581 -0.57882  0.48196 ... -0.04163 -0.36621 -0.01844]
# i [-0.23092 -0.45225  0.0791  ... -0.10318 -0.09371 -0.01335]
# j [-0.2118  -0.49759  0.33551 ...  0.04639 -0.22614 -0.01955]
# k [-0.2331  -0.68341  0.11294 ... -0.21091 -0.28575  0.03335]
# l [ 0.13276 -0.53209  0.50743 ...  0.42919 -0.18398  0.18368]
# m [ 0.10097 -0.51353  0.35599 ...  0.15404  0.05567  0.28163]
# n [-0.11253 -0.56633  0.54002 ... -0.27129 -0.11794  0.21983]
# o [-0.18439 -0.31817  0.26147 ...  0.00808 -0.34414 -0.03903]
# p [-0.15042 -0.88944  0.18703 ... -0.50027 -0.11908  0.079  ]
# q [-0.5497  -0.59806  0.68132 ... -0.47467 -0.47433  0.02084]
# r [-0.14467 -0.36121  0.43144 ...  0.04704 -0.14087 -0.09054]
# s [-0.30696 -0.52904  0.56251 ... -0.24135 -0.01464  0.25233]
# t [-0.34611 -0.75995  0.55582 ... -0.28527 -0.01619  0.1874 ]
# u [-0.34462 -0.68102  0.55081 ... -0.04176 -0.27297  0.33628]
# v [-0.04387 -0.39901  0.44572 ...  0.13509 -0.22151  0.04325]
# w [-0.23551 -0.82211  0.60162 ... -0.0018  -0.098    0.13925]
# x [-0.48844 -0.50041  0.48628 ...  0.22434 -0.70783  0.06925]
# y [-0.63024 -0.53356  0.52819 ... -0.04966 -0.45855 -0.07299]
# z [-0.44457 -0.79942  0.04594 ... -0.12839 -0.51991 -0.07331]
# A [-0.0659  -0.25593  0.07183 ...  0.0188   0.07331 -0.15115]
# B [-0.50557 -0.58696  0.27922 ... -0.05495  0.07553 -0.02364]
# C [-0.26717 -0.61295  0.12418 ...  0.05005  0.05811 -0.16858]
# D [-0.37951 -0.30074  0.35125 ...  0.10091  0.07058 -0.0061 ]
# E [-0.10301 -0.40931  0.12072 ...  0.07883  0.23783  0.11427]
# F [-0.38514 -0.49403  0.41834 ... -0.29458  0.18312  0.01765]
# G [-0.45476 -0.55236  0.4817  ... -0.18496  0.09052 -0.01888]
# H [-0.43212 -0.63836  0.41607 ... -0.15043  0.02371 -0.01874]
# I [ 0.01567 -0.75617  0.00754 ... -0.21828  0.09834 -0.02001]
# J [-0.38662 -0.69848  0.07406 ... -0.42653 -0.29967 -0.3886 ]
# K [-0.39989 -0.75427  0.04993 ... -0.52456 -0.21794 -0.27881]
# L [-0.02717 -0.05113  0.35996 ...  0.22993  0.14099  0.07733]
# M [-0.38595 -0.66086  0.36416 ... -0.11637  0.00795 -0.00343]
# N [-0.64072 -0.18584  0.28048 ... -0.67034  0.25577  0.78077]
# O [-0.19793 -0.37288  0.29932 ... -0.10041 -0.00666 -0.06876]
# P [ 0.17183 -0.57317  0.13991 ... -0.29749  0.01394 -0.05255]
# Q [-0.50811 -0.41047  0.68427 ... -0.39648 -0.06948 -0.06467]
# R [-0.12877 -0.48751  0.40246 ... -0.09281  0.18291 -0.23491]
# S [-0.06767 -0.38757  0.19151 ... -0.1576   0.08183  0.03963]
# T [-0.36513 -1.63166  0.67466 ... -0.29936  0.36167  0.06867]
# U [ 0.14986 -0.36397  0.09402 ... -0.16042 -0.3351   0.02279]
# V [-0.33591 -0.41282  0.16495 ... -0.14412 -0.00554 -0.28744]
# W [-0.54861 -0.75428  0.56476 ... -0.69048  0.09681 -0.28834]
# X [-0.56594 -0.64557  0.41885 ...  0.13301 -0.25761 -0.22189]
# Y [-0.42792 -0.47828  0.26549 ... -0.12525 -0.40901 -0.29147]
# Z [-0.1714  -0.7279   0.07252 ... -0.3086   0.06965 -0.51548]
# ! [-0.06463 -0.89681 -0.21493 ... -0.44736 -0.19379 -0.18691]
# " [-0.13306 -0.47879  0.19418 ... -0.58434 -0.01341  0.03904]
# # [-0.01133 -0.27309  0.3152  ... -0.79558 -0.13951 -0.22416]
# $ [-0.03892 -0.50797 -0.19612 ... -0.23744  0.1344  -0.1735 ]
# % [-0.12228  0.2462   0.39928 ... -0.41348  0.30946  0.01399]
# & [-0.41713 -0.42194  0.60497 ... -0.44294 -0.02798 -0.21172]
# ' [-0.3064  -0.49213  0.15721 ... -0.7445   0.2183  -0.0231 ]
# ( [-0.00679 -0.44517  0.1225  ... -0.78359  0.06795 -0.1614 ]
# ) [-0.1084  -0.29203  0.44453 ... -0.73722 -0.07482 -0.39144]
# * [-0.20952 -0.58466  0.52112 ... -0.10662 -0.01636 -0.1114 ]
# + [-0.30848 -0.4114   0.65979 ... -0.51248  0.07804 -0.20564]
# , [-0.28954 -0.58278  0.01444 ... -0.67303  0.05786 -0.2376 ]
# - [ 0.03846 -0.73439  0.06152 ... -0.73059 -0.39709 -0.073  ]
# . [-0.35124 -0.81085  0.30611 ... -0.71134  0.05895  0.07077]
# / [-0.17542 -1.14299  0.45079 ... -0.35878  0.23163 -0.04131]
# : [-0.26284 -0.35803  0.5692  ... -0.43358  0.10031 -0.24573]
# ; [-0.46372 -0.65403  0.20618 ... -0.45915 -0.24919 -0.03192]
# < [-0.50874 -0.71019  0.15737 ... -0.61117 -0.03463 -0.06567]
# = [-0.49531 -0.28307  0.63305 ... -0.53501 -0.11268 -0.25714]
# > [-0.5843  -0.79314  0.13807 ... -0.68858 -0.06544 -0.22157]
# ? [-0.56853 -0.63903 -0.01355 ... -0.26429 -0.05392 -0.15432]
# @ [-0.53462 -0.11569  0.02156 ... -0.56672 -0.24822 -0.14534]
# [ [ 0.03686 -0.27973  0.61888 ... -0.75483  0.22337 -0.20013]
# \ [-0.32091 -0.22062  0.24325 ... -0.37931 -0.49664 -0.35213]
# ] [-0.23616 -0.54913  0.19286 ... -0.5066  -0.2297  -0.31172]
# ^ [-0.50199 -0.29384  0.3911  ... -0.43294 -0.44525 -0.06177]
# _ [-0.02125 -0.46235  0.12849 ... -0.63582  0.0622  -0.41226]
# ` [-0.14099  0.19925 -0.10219 ...  0.16749  0.10886  0.55444]
# { [-0.61644 -0.4441  -0.16222 ... -0.69598 -0.45594 -0.05108]
# | [-0.52918 -0.48273  0.04762 ... -0.50454 -0.3325   0.06426]
# } [-0.04085 -0.36607  0.08122 ... -0.49751 -0.16179  0.1242 ]
# ~ [ 0.23849 -0.51369  0.1579  ... -0.74759 -0.3237   0.00188]
#   [-0.18707  0.09738 -0.12419 ... -0.8026  -0.24748  0.84416]
# \n [-0.18707  0.09738 -0.12419 ... -0.8026  -0.24748  0.84416]
# \t [-0.18707  0.09738 -0.12419 ... -0.8026  -0.24748  0.84416]
# \r [-0.18707  0.09738 -0.12419 ... -0.8026  -0.24748  0.84416]
# \v [-0.18707  0.09738 -0.12419 ... -0.8026  -0.24748  0.84416]
# \f [-0.18707  0.09738 -0.12419 ... -0.8026  -0.24748  0.84416]