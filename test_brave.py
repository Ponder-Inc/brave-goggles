import pdb
import os
from dotenv import load_dotenv
load_dotenv()

from brave import Brave
BRAVE_API_KEY = os.getenv("BRAVE_API_KEY")
brave_client = Brave()
goggle_url = "https://raw.githubusercontent.com/Ponder-Inc/brave-goggles/main/ponder_arxiv_hause_citations.txt"

# query = "Were the Los Angeles fires natural wildfires or acts of arson?"
query = "Los Angeles fires due to arson"

search_results = brave_client.search(q=query, goggles_id=goggle_url, count=50)

pdb.set_trace()
