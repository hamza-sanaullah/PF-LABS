#Write a program that takes bytes from the user and convert it into Mega Bytes and Giga Bytes

BYTES = int(input("Enter Bytes:"))
#CONVERSION INTO MEGA BYTES


mega_bytes = BYTES / (2**20)
print(f"The mega bytes are {mega_bytes}")

# CONVERSION INTO GIGA BYTES
giga_bytes = BYTES / (2**30)
print(f"The giga bytes are {giga_bytes}")











