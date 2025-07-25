import random 
import string
CHARACTER_SET = string.ascii_letters + string.digits
def generate_short_code(length=6):
	generated_code = "".join(random.choices(CHARACTER_SET, k=length))
	return generated_code

if __name__ == "__main__":
	print(" --- test generate_short_code --- ")
	print("generateing short code of length (6)")
	for i in range(5):
		print("\\n" +"-"* 20+ "\\n")
		print("generating 1code with custom length (10):")
		print(generate_short_code(length=10))
		print("\\n"+"--- test complete ---")