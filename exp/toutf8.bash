for file in *.txt; do
    iconv -f ascii -t utf-8 "$file" -o "${file%.txt}.utf8.txt"
done