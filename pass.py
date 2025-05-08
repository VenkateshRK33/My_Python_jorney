import re

# Example text containing email addresses
text = "Hello from abc199630@gmail.com to xyz456@yahoo.com about the meeting @2PM"

# Regex pattern to extract email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[gmailyahoo]+.[com]'

# Finding all matches
emails = re.findall(email_pattern, text)

# Printing extracted emails
print("Extracted Email IDs:", emails)
