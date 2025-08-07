import argparse
from fetcher.fetch import fetch_data
from utils.writer import write_data

DEFAULT_COLUMNS = ["rank", "country", "company", "city"]

def main():
    parser = argparse.ArgumentParser(description="Fortune 500 Scraper Tool")
    parser.add_argument('--output', choices=['excel', 'csv'], default='excel', help='Output format')
    parser.add_argument('--columns', nargs='+', help='Columns to extract', default=DEFAULT_COLUMNS)

    args = parser.parse_args()

    print("📥 Fetching data...")
    raw_data = fetch_data()

    print("🔍 Processing data...")
    rows = []
    for item in raw_data:
        row = [item.get(col, "") for col in args.columns]
        rows.append(row)

    filename = f"fortune500_output.{ 'xlsx' if args.output == 'excel' else 'csv' }"
    print(f"💾 Saving to {filename}...")
    write_data(rows, args.columns, filename, args.output)

    print(f"✅ Done! Saved {len(rows)} rows to {filename}.")

if __name__ == "__main__":
    main()