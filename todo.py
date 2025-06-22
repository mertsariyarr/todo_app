import argparse
def main():
    print("Merhaba bu bir görev takip uygulamasidir.")
    parser = argparse.ArgumentParser()
    parser.add_argument("--add")
    args = parser.parse_args()
    if args.add:
        print(f"Görev Eklendi: {args.add}")
    else:
        print("Hiçbir görev eklenmedi.")
main()