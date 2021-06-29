#This script is optimized for images with a monocolor background. Works most of the time.
file=$1
tmp="${file%%.*}.ppm"
svg="${file%%.*}.svg"
#1) Convert to ppm
mogrify -format ppm $1 >/dev/null 2>&1
convert $1 -fill none -fuzz 7% -draw 'matte 0,0 floodfill' -flop  -draw 'matte 0,0 floodfill' -flop -normalize $tmp >/dev/null 2>&1

#2) Extract svg
potrace -s $tmp >/dev/null 2>&1
#delete tmp 
rm $tmp >/dev/null 2>&1

#3) Minimize svg
svgo -i $svg >/dev/null 2>&1

#4) Extract paths
cat $svg | grep -Eo 'd="[^\"]+"' | cut -c 4- |  sed 's/.$//'
