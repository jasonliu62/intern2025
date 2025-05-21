from update import update_incorporation_state

def main():
    html_path = "msft-20250430.htm"
    xsd_path = "msft-20250430.xsd"

    print("Current state: Washington")  # You can fetch this dynamically if needed.
    new_state = input("Enter the new incorporation state (e.g., Delaware): ").strip()

    if not new_state:
        print("No state entered. Aborting.")
        return

    update_incorporation_state(html_path, xsd_path, new_state)
    print(f"Updated incorporation state to: {new_state}")

if __name__ == "__main__":
    main()
