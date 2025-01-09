import pdb
import os
import pandas as pd

# Read the CSV file
df = pd.read_csv('domain_pc1.csv')

df = df[df['pc1'] >= 0.8]

credible_domains = df['domain'].tolist()

exclude_domains = [
    "youtube.com",
    "facebook.com",
    "instagram.com",
    "twitter.com",
    "linkedin.com",
    "reddit.com",
    "pinterest.com",
    "tumblr.com",
    "medium.com",
    "quora.com",
    "blogger.com",
    "wordpress.com",
]

downrank_domains = [
    "*/blogs/*",
    "*/blog/*",
]

boost_domains = [
    "*.edu",
    "*.gov",
    "*.org"
]

with open("domains.txt", "w") as f:

    f.write(f"\n! Hause Lin's Domains pc1 >= 0.8 \n")
    for domain in credible_domains:
        boost_string = f"site={domain}$boost=10"
        f.write(boost_string + "\n")
    
    f.write(f"\n! Boosted Credible Domain Suffixes \n")
    f.write("\n")

    for domain in boost_domains:
        boost_string = f"site={domain}$boost=3"
        f.write(boost_string + "\n")

    f.write(f"\n! Excluded Domains \n")
    f.write("\n")

    for domain in exclude_domains:
        discard_string = f"site={domain}$discard"
        f.write(discard_string + "\n")
    
    f.write(f"\n! Downranked Domain Suffixes \n")
    f.write("\n")

    for domain in downrank_domains:
        downrank_string = f"site={domain}$downrank=10"
        f.write(downrank_string + "\n")
    
    f.close()