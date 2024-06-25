def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    z = input()
    h = convert(z)
    print(h)

if __name__ == "__main__":
    main()
