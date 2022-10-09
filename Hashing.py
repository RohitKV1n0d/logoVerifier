import hashlib

def main():
    
    text = "hfckfclgclhggclfclgclgcljgcljgcjlgcljgcv;gc"
    textut8 = text.encode("utf-8")

    hash = hashlib.md5(textut8)
    hexa = hash.hexdigest()

    print(hexa)

    return

main()