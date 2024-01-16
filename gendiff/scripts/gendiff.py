import argparse

parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
group = parser.add_mutually_exclusive_group()
group.add_argument("-f FORMAT", "--format FORMAT", action="store_true", help = "set format of output")
#group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("first_file")
parser.add_argument("second_file")
args = parser.parse_args()
answer = f'{args.first_file} {args.second_file}' 


def main():
    if args.quiet:
        print(answer)
    elif args.format:
        print(f"compare {args.first_file} and {args.second_file}")
    else:
        print(f"diff {args.first_file} {args.second_file} == {answer}")
    
if __name__ == '__main__':
    main() 