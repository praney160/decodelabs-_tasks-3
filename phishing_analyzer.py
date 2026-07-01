# DecodeLabs Project 3
# Phishing Awareness Analysis

red_flags = [
    "urgent",
    "verify",
    "password",
    "bank",
    "click here",
    "login",
    "winner",
    "free",
    "gift",
    "account suspended",
    "limited time",
    "http://",
    "https://"
]

print("=" * 50)
print("      PHISHING AWARENESS ANALYZER")
print("=" * 50)

message = input("\nPaste the email/message:\n\n")

found = []

for flag in red_flags:
    if flag.lower() in message.lower():
        found.append(flag)

print("\nAnalysis Result")
print("-" * 40)

if found:
    print("⚠️ Potential Phishing Detected!\n")
    print("Red Flags Found:")
    for item in found:
        print("•", item)

    print("\nWhy is it unsafe?")
    print("- It contains words commonly used in phishing attacks.")
    print("- It may try to steal personal information.")
    print("- Never click suspicious links or share passwords.")
else:
    print("✅ No obvious phishing indicators detected.")