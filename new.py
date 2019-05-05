import re
line="乃使使割adsad243524河西之, 地献于秦以和€。"
linec=re.findall(r"[\w']+", line)
print(linec)
result=" ".join(linec)
print(result)