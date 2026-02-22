import phonenumbers
from phonenumbers import geocoder, carrier
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + "=" * 50)
print(Fore.YELLOW + "📍 PHONE NUMBER INFORMATION SYSTEM")
print(Fore.CYAN + "=" * 50)

try:
    # INPUT SECTION
    number = input(Fore.GREEN + "\nEnter Phone Number with Country Code: ")

    parsed_number = phonenumbers.parse(number, None)

    # VALIDATION
    is_valid = phonenumbers.is_valid_number(parsed_number)
    location = geocoder.description_for_number(parsed_number, "en")
    service_provider = carrier.name_for_number(parsed_number, "en")

    # OUTPUT SECTION
    print(Fore.CYAN + "\n" + "-" * 40)
    print(Fore.YELLOW + "📞 NUMBER DETAILS")
    print(Fore.CYAN + "-" * 40)

    print(Fore.WHITE + f"{'Number:':18} {number}")
    print(Fore.WHITE + f"{'Location:':18} {location}")
    print(Fore.WHITE + f"{'Service Provider:':18} {service_provider}")
    print(Fore.WHITE + f"{'Valid Number:':18} {is_valid}")

    print(Fore.CYAN + "=" * 50)
    print(Fore.GREEN + "✅ Process Completed Successfully")
    print(Fore.CYAN + "=" * 50)

except Exception as e:
    print(Fore.RED + "\n❌ Error:", e)