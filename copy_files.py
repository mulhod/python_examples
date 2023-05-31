from os import makedirs


def main():
    file_name = "test.txt"
    makedirs("clones", exist_ok=True)
    file = open(file_name)
    text = file.read()
    for i in range(1, 101):
       new_file = open("clones/" + str(i) + ".txt", "w")
       new_file.write("This is the text in " + file_name + ": " + text)

if __name__ == "__main__":
    main()

