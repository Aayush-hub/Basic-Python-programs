import random

Lower="abcdefghijklmnopqrstuvwxyz"
Upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Number="1234567890"
Symbols="~`!@#$%^&*()_+-=\|[];',./{}:<>?*/"

All=Lower+Upper+Number+Symbols
Length=16

Password="".join(random.sample(All, Length))
print("Suggested password is :")
print(Password)