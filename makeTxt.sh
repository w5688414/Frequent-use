# /usr/bin/env sh
DATA=/home/eric/data/deepdrive/bdd100k/images/100k/train/
DATASAVE=/home/eric/data/deepdrive/bdd100k/VOCdevkit
echo "Create train.txt..."
find $DATA -name *.jpg | cut -d '/' -f10 | cut -d '.' -f1>>$DATASAVE/train.txt
echo "Done.."

VALDATA=/home/eric/data/deepdrive/bdd100k/images/100k/val/
VALDATASAVE=/home/eric/data/deepdrive/bdd100k/VOCdevkit
echo "Create val.txt..."
find $VALDATA -name *.jpg | cut -d '/' -f10 | cut -d '.' -f1>>$VALDATASAVE/val.txt
echo "Done.."