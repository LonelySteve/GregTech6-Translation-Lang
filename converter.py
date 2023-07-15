import re
from io import TextIOWrapper

keySet = set()

RE_LINE = re.compile(r"\s*S:\"?(?P<key>([^\"=]*))\"?=(?P<value>(.*))\s*")
 
def handle_line(line: str):
    match = RE_LINE.match(line)
    if match is not None:
        key = match.group("key")
        value = match.group("value")
        
        key = re.sub(r"\.name$", "", key)

        # 去重
        if key in keySet:
            return
        
        keySet.add(key)

        if " " in key:
            return f'    S:"{key}"={value}\n'
        else:
            return f"    S:{key}={value}\n"
            
def handle(fp_i: TextIOWrapper , fp_o: TextIOWrapper):
    for line in fp_i:
        if re.match(r"\s*S:", line):
            output = handle_line(line)
            if output:
                fp_o.write(output)
        else:
            fp_o.write(line)


if __name__ == "__main__":
    with open("./gregtech.lang", "w", encoding="utf-8") as fp_o:
        with open("./GregTech-TeamNED.lang", "r", encoding="utf-8") as fp_i:
            handle(fp_i, fp_o)
