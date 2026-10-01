from pathlib import Path
from urllib.request import Request, urlopen

URL = (
    "https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/"
    "Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat"
)
OUT = Path(__file__).resolve().parents[1] / "data" / "Pantheon+SH0ES.dat"

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    print("Downloading official Pantheon+ data...")
    req = Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=60) as response:
        content = response.read()
    OUT.write_bytes(content)
    print(f"Saved {len(content):,} bytes to {OUT}")

if __name__ == "__main__":
    main()
