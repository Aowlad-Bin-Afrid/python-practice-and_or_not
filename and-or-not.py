# ==========================================
# Logical Operators: AND, OR, NOT in Python
# Real-Life Examples for Beginners
# ==========================================

# ------------------------------------------
# 1️⃣ AND Operator Example – Voting Eligibility
# ------------------------------------------

age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ").lower()

# To vote, you must be at least 18 years old AND be a citizen
if age >= 18 and citizen == "yes":
    print("✅ You are eligible to vote.")
else:
    print("❌ You are not eligible to vote.")


# ------------------------------------------
# 2️⃣ OR Operator Example – Login System
# ------------------------------------------

username = input("\nEnter your username: ")
email = input("Enter your email: ")

# Login succeeds if either the username OR email matches
if username == "admin" or email == "admin@example.com":
    print("🔐 Login successful! Welcome, Admin.")
else:
    print("🚫 Invalid login credentials.")


# ------------------------------------------
# 3️⃣ NOT Operator Example – Internet Connection Check
# ------------------------------------------

wifi_connected = input("\nIs your WiFi connected? (yes/no): ").lower()

# Internet is available only if WiFi is NOT disconnected
if not (wifi_connected == "yes"):
    print("⚠️ Please connect to WiFi to access the internet.")
else:
    print("🌐 You are connected to the internet.")


# ------------------------------------------
# 4️⃣ Combined Example – Online Shopping Discount
# ------------------------------------------

is_member = input("\nAre you a member? (yes/no): ").lower()
has_coupon = input("Do you have a discount coupon? (yes/no): ").lower()
cart_total = float(input("Enter your total cart amount: "))

# Discount applies if user is a member with a bill over 500 OR has a coupon
if (is_member == "yes" and cart_total > 500) or has_coupon == "yes":
    print("💸 You get a discount on your purchase!")
else:
    print("❌ No discount available.")


# ------------------------------------------
# 5️⃣ NOT + AND Example – Game Over Logic
# ------------------------------------------

player_health = int(input("\nEnter your player health: "))
time_left = int(input("Enter remaining game time (in seconds): "))

# Game ends if health is zero OR time runs out
if not (player_health > 0 and time_left > 0):
    print("💀 Game Over!")
else:
    print("🔥 Keep playing! You’re still in the game.")
